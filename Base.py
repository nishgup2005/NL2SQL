from typing import TypedDict, Annotated

class State(TypedDict):
    question: str
    query: str
    result: str
    ans: str

class QueryOutput(TypedDict):
    """Generated SQL Query"""
    query: Annotated[str, ..., "Structured Syntactically correct Query Output"]