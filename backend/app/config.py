from pydantic import BaseSettings, AnyHttpUrl
from typing import List


class Settings(BaseSettings):
    mongodb_uri: str = "mongodb://localhost:27017"
    mongodb_db: str = "policy_lens"
    firebase_project_id: str = ""
    firebase_credentials_path: str = ""
    openai_api_key: str = ""
    chroma_persist_directory: str = "./backend/chromadb"
    frontend_origins: List[AnyHttpUrl] = ["http://localhost:4200"]
    environment: str = "development"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
