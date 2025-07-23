from langchain_core.runnables import RunnableBranch, RunnableLambda
from NL2SQL.settings.config import llm
from NL2SQL.utils import generate_state_intent, generate_state_query, get_invalid_state, get_clarity_state, execute_query, suppressWarnings, printState
from NL2SQL.Base import IntentOutput, QueryOutput, AnsOutput
from NL2SQL.prompts import IntentPrompt, RetrievalPrompt, DescPrompt, AscPrompt, AggPrompt, SubQueryPrompt, AnsPrompt
suppressWarnings()

intent_prompt = IntentPrompt.prompt
retr_prompt = RetrievalPrompt.prompt
asc_prompt = AscPrompt.prompt
desc_prompt = DescPrompt.prompt
agg_prompt = AggPrompt.prompt
sub_prompt = SubQueryPrompt.prompt
ans_prompt = AnsPrompt.prompt

intent_llm = llm.with_structured_output(IntentOutput)
query_llm = llm.with_structured_output(QueryOutput)
ans_llm = llm.with_structured_output(AnsOutput)

intent_chain = intent_prompt |  intent_llm | generate_state_intent

gen_query_chain = query_llm | generate_state_query 

gen_agg_query_chain = agg_prompt | gen_query_chain
gen_asc_query_chain = asc_prompt | gen_query_chain
gen_desc_query_chain = desc_prompt | gen_query_chain
gen_retr_query_chain = retr_prompt | gen_query_chain
gen_sub_query_chain = sub_prompt | gen_query_chain 
clarity_chain = RunnableLambda(get_clarity_state)
invalid_chain = RunnableLambda(get_invalid_state)

branch = RunnableBranch(
    (lambda state: state["intent"]==1,gen_retr_query_chain),
    (lambda state: state["intent"]==2,gen_asc_query_chain),
    (lambda state: state["intent"]==3,gen_desc_query_chain),
    (lambda state: state["intent"]==4,gen_agg_query_chain),
    (lambda state: state["intent"]==5,gen_sub_query_chain),
    (lambda state: state["intent"]==6,clarity_chain),
    invalid_chain # default / fallback
    )


execute_chain = RunnableLambda(execute_query)

ans_chain = ans_prompt |  ans_llm 

final_chain = intent_chain | RunnableLambda(printState) | branch | RunnableLambda(printState) | execute_chain | RunnableLambda(printState) | ans_chain