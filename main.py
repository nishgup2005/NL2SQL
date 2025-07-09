from langchain.chat_models import init_chat_model
from langchain_community.utilities import SQLDatabase
from NL2SQL.settings.config import Config
from NL2SQL.utils import generate_query, execute_query
import os

db = SQLDatabase.from_uri(Config.DATABASE_URI)

os.environ["GOOGLE_API_KEY"] = Config.GEMINI_API_KEY

llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

question = input("Enter Your Question here: ")

state = {"question": question}

state = generate_query(state=state, db=db, top_k="all", llm=llm)
state = execute_query(db, state)

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
