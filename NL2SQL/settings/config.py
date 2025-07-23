from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from langchain_community.utilities import SQLDatabase
from langchain.chat_models import init_chat_model


class Setting(BaseSettings):
    GEMINI_API_KEY: str
    DATABASE_URI: str
    SQLALCHEMY_DATABASE_URL: str
    SECRET_KEY: str
    HASH: str
    TIME_TO_LIVE: int = 30
    EMAIL_SECRET_KEY: str
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_PORT: int
    MAIL_SERVER: str
    MAIL_FROM_NAME: str
    MAIL_STARTTLS: bool = True
    MAIL_SSL_TLS: bool = False
    USE_CREDENTIALS: bool = True
    VALIDATE_CERTS: bool = True
    TEMPLATE_FOLDER: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


Config = Setting()

db = SQLDatabase.from_uri(Config.DATABASE_URI)
os.environ["GOOGLE_API_KEY"] = Config.GEMINI_API_KEY
llm = init_chat_model(model="gemini-2.0-flash", model_provider="google_genai")
