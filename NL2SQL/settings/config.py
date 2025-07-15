from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from langchain_community.utilities import SQLDatabase
from langchain.chat_models import init_chat_model


class Setting(BaseSettings):
    GEMINI_API_KEY: str
    DATABASE_URI: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


Config = Setting()

db = SQLDatabase.from_uri(Config.DATABASE_URI)
os.environ["GOOGLE_API_KEY"] = Config.GEMINI_API_KEY
llm = init_chat_model(model="gemini-2.0-flash", model_provider="google_genai")
