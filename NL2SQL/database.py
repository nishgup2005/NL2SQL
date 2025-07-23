from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from NL2SQL.settings.config import Config
from langchain_community.utilities import SQLDatabase

# URL used to link the provide the route to the database
SQLALCHEMY_DATABASE_URL = Config.SQLALCHEMY_DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# get db function used to safely get a database connection
def get_db():
    db = session()
    try:
        yield db
    finally:
        del db
