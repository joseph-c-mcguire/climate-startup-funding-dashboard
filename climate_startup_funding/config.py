import os
from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    CRUNCHBASE_API_KEY: str = os.getenv("CRUNCHBASE_API_KEY", "")
    ANGELLIST_API_KEY: str = os.getenv("ANGELLIST_API_KEY", "")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///data.db")
    
    class Config:
        env_file = ".env"

settings = Settings()
