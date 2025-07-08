import langchain_openai, langsmith
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.utilities import SQLDatabase
from NL2SQL.settings.config import Config
from NL2SQL.Base import State, QueryOutput
from NL2SQL.utils  import generate_prompt, execute_query
import os
from typing import Annotated

db = SQLDatabase.from_uri(Config.DATABASE_URI)
# print(type(db.dialect))
# print(db.get_usable_table_names())
# print(type(db.table_info))
# print(db.run("select * from employees;"))

os.environ["GOOGLE_API_KEY"] = Config.GEMINI_API_KEY
llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai")
while (True):
    question = input("Enter Your Question here: ")
    if question in ["exit", None]:
        break
    state = {"question":question}

    prompt = generate_prompt(state=state, db=db, top_k="all")
    struct_llm = llm.with_structured_output(QueryOutput)
    query = struct_llm.invoke(prompt)

    state["query"] = query['query']
    state = execute_query(db,state)

    """Answer question using retrieved information as context."""
    prompt = (
            "Given the following user question, corresponding SQL query, "
            "and SQL result, answer the user question.\n\n"
            f'Question: {state["question"]}\n'
            f'SQL Query: {state["query"]}\n'
            f'SQL Result: {state["result"]}'
        )

    response = llm.invoke(prompt)
    state["ans"] = response.content

    print(state)