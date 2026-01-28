import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

# Base directory
BASE_DIR = Path(__file__).resolve().parents[2]

# Load .env file from project root
env_path = BASE_DIR / ".env"
if env_path.exists():
    load_dotenv(env_path)
    print(f".env loaded from {env_path}")
else:
    print("Warning: .env file not found at", env_path)

class Settings(BaseSettings):
    app_name: str = Field(env="app_name")
    env: str = Field(env="env")
    database_url: str = Field(env="database_url")
    secret_key: str = Field(env="secret_key")
    algorithm: str = Field(env="algorithm")
    access_token_expire_minutes: int = Field(env="access_token_expire_minutes")

    # Ignore extra variables in .env
    model_config = SettingsConfigDict(extra="ignore")

# Instantiate settings
settings = Settings()

# DEBUG output
print("Settings loaded successfully!")
print("APP_NAME:", settings.app_name)
print("ENV:", settings.env)
print("DATABASE_URL:", settings.database_url)
