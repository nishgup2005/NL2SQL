from langchain_core.prompts import ChatPromptTemplate
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from langchain_community.utilities import SQLDatabase
from NL2SQL.Base import State, QueryOutput

systemMsg = """
**FALLBACK : If the query seems unrelated to the database then simply return "Sorry i couldn't understand the query"
Given an input question, create a syntactically correct {dialect} query to
run to help find the answer. Unless the user specifies in his question a
specific number of examples they wish to obtain, always limit your query to
at most {top_k} results. You can order the results by a relevant column to
return the most interesting examples in the database.

Never query for all the columns from a specific table, only ask for a the
few relevant columns given the question.

Pay attention to use only the column names that you can see in the schema
description. Be careful to not query for columns that do not exist. Also,
pay attention to which column is in which table.

Only use the following tables:
{table_info}"""

userMsg = """Question: {input}"""

QueryPromptTemplate = ChatPromptTemplate([("system",systemMsg), ("user",userMsg)])

def generate_query(db: SQLDatabase, state: State, top_k: int, llm: BaseChatModel) -> State:
    prompt = QueryPromptTemplate.invoke(
        {
            "dialect": db.dialect,
            "top_k": top_k,
            "table_info": db.table_info,
            "input": state["question"]
        }
    )
    struct_llm = llm.with_structured_output(QueryOutput)
    query = struct_llm.invoke(prompt)
    state["query"] = query['query']
    return state

def execute_query(db: SQLDatabase, state: State):
    execute_query_tool = QuerySQLDataBaseTool(db=db)
    result = execute_query_tool.invoke(state["query"])
    state["result"] = result
    return state
