from pydantic_settings import BaseSettings, SettingsConfigDict


class Setting(BaseSettings):
    GEMINI_API_KEY: str
    DATABASE_URI: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


Config = Setting()
