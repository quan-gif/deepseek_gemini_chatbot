from functools import lru_cache
from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    gemini_api_key:str
    gemini_model:str = "gemini-3.8-flash"
    deepseek_api_key:str
    deepseek_base_url:str = "https://api.deepseek.com"
    model_name:str = "deepseek-chat"
    max_tokens:int = 1024
    model_config = SettingsConfigDict(
        env_file = ".env",
        env_file_encoding = "utf-8",
        case_sensitive = False,
        extra = 'ignore'

    )
@lru_cache
def get_settings() -> Settings:
    return Settings()
settings = get_settings()



