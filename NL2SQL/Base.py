from typing import TypedDict, Annotated
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_community.utilities import SQLDatabase

class State(TypedDict):
    intent: int
    llm: BaseChatModel
    db: SQLDatabase
    question: str
    schema: str
    query: str
    result: str
    ans: str

class QueryOutput(TypedDict):
    """Generated SQL Query"""
    query: Annotated[str, ..., "Structured Syntactically correct Query Output"]
    relevant_tables: Annotated[list[str],...,"List of tables which are provided in the prompt"]
    question: Annotated[str, ..., "The Questions asked by user in the prompt"]

class IntentOutput(TypedDict):
    """Generated intent and list of relevant tables"""
    intent: Annotated[int,...,"The intent of the question"]
    relevant_tables: Annotated[list[str],...,"List of tables which are relevant to the question"]
    question: Annotated[str, ..., "The Correct Version of the Question asked by the user"]

class AnsOutput(TypedDict):
    """Generated Answer by interpreting the Question Query and Result"""
    result:Annotated[str, ..., "A well Formated structured form of the result in english language"]