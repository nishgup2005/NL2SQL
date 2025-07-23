from fastapi import FastAPI
from NL2SQL.utils import db, format
from NL2SQL.chains import final_chain
from fastapi.responses import JSONResponse
from datetime import datetime
from NL2SQL.dependency import db_dependency, user_dependency
import json
import os
from redis import Redis, ConnectionPool
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app:FastAPI):
    app.state.redis = Redis(connection_pool=ConnectionPool(host='localhost', port=6379))
    print("redis estabilished")
    yield
    app.state.redis.close()

app = FastAPI(lifespan=lifespan)


@app.get("/")
def welcome():
    return{"helloworld"}

@app.get("/chat/{question}")
def query(question:str, user_db:db_dependency, user:user_dependency, sessionID:str = "4"):
    filename = f"memory/{user.id}.json"
    user_chat={}
    chat_history = {}
    if os.path.exists(filename):
        with open(filename, "r") as f:
            data = f.read()
            if len(data)!=0:
                user_chat=json.loads(data)
                if sessionID in user_chat.keys():
                    chat_history = user_chat[sessionID]
                    print(chat_history)
    response = ""
    if question is not None and question.lower().strip() not in ["exit","escape","quit"]:
        response = final_chain.invoke({
            "question": question,
            "dialect": db.dialect,
            "table_names":db.get_usable_table_names(),
            "chat_history":{i:chat_history[i] for i in list(chat_history.keys())[-5:]}
            })
        print(response)

    # Memory insertion here
        chat_history[datetime.now().strftime(format)] = {"question":question,"answer":response, "timestamp":datetime.now().strftime(format)}
    else:
        chat_history[datetime.now().strftime(format)] = {"question":question, "answer": f"User has ended the conversation","timestamp":datetime.now().strftime(format)}
    user_chat[sessionID] = chat_history

    with open(filename,"w") as f:
        user_data = json.dumps(user_chat)
        f.write(user_data)
    return JSONResponse(content={"status_code":200,
                                 "response":response},
                        status_code=200)