from langchain_community.tools.sql_database.tool import QuerySQLDatabaseTool
from NL2SQL.Base import State, QueryOutput, IntentOutput
from NL2SQL.settings.config import db, llm
from pprint import pprint

def execute_query(state: State):
    if state["query"]!="":
        execute_query_tool = QuerySQLDatabaseTool(db=db)
        result = execute_query_tool.invoke(state["query"])
        state["result"] = result
    return state


def generate_state_intent(response:IntentOutput):
    state : State = {
    "dialect":db.dialect,
    "intent":response["intent"],
    "llm":llm,
    "db":db,
    "prompt":"",
    "question":response["question"],
    "schema":db.get_table_info(response["relevant_tables"]),
    "query":"",
    "result":"",
    "ans":""
}
    return state

def generate_state_query(response:QueryOutput):
    state : State = {
    "dialect":db.dialect,
    "intent":"",
    "llm":llm,
    "db":db,
    "prompt":"",
    "question":response["question"],
    "schema":db.get_table_info(response["relevant_tables"]),
    "query":response["query"],
    "result":"",
    "ans":""
}
    return state

def get_clarity_state(state: State):

    state:State = {
    "dialect":db.dialect,
    "intent":state["intent"],
    "llm":state["llm"],
    "db":state["db"],
    "prompt":"",
    "question":state["question"],
    "schema":state["schema"],
    "query":"",
    "result":"The Question seems a little confusing \nCould you please try asking the question again with more detail",
    "ans":"The Question seems a little confusing \nCould you please try asking the question again with more detail"
    }

    return state

def get_invalid_state(state: State):

    state:State = {
    "dialect":db.dialect,
    "intent":state["intent"],
    "llm":state["llm"],
    "db":state["db"],
    "prompt":"",
    "question":state["question"],
    "schema":state["schema"],
    "query":"",
    "result":"It appears that your question is out of the scope for my knowledge \nPlease try asking another question",
    "ans":"It appears that your question is out of the scope for my knowledge \nPlease try asking another question"
    }

    return state

def suppressWarnings():
    import warnings
    from sqlalchemy.exc import SAWarning

    warnings.filterwarnings(
        "ignore",
        message="Cannot correctly sort tables; there are unresolvable cycles between tables",
        category=SAWarning
    )

def printState(state:State):
    pprint(state)
    return (state)