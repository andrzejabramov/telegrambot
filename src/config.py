from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    TOKEN_BOT: str
    model_config = SettingsConfigDict(env_file='../.env')

settings = Settings()
