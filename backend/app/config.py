"""Application Configuration"""

import os
from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""

    # App Info
    APP_NAME: str = "iCARexpert"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = True
    ENVIRONMENT: str = "development"

    # Database
    DATABASE_URL: str = "sqlite:///./icarexpert.db"
    SQLALCHEMY_ECHO: bool = False

    # LLM Configuration (Ollama)
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "llama2:7b-chat-q4_K_M"
    OLLAMA_TIMEOUT: int = 300
    OLLAMA_NUM_GPU: int = 1

    # Email Configuration
    SMTP_SERVER: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USERNAME: str = ""
    SMTP_PASSWORD: str = ""
    SMTP_FROM_EMAIL: str = "icarexpert@example.com"
    SMTP_FROM_NAME: str = "iCARexpert AI"

    # Scraping Configuration
    SCRAPER_ENABLED: bool = True
    SCRAPER_DELAY: int = 2
    USER_AGENT: str = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )

    # Security
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "logs/icarexpert.log"

    # Spanish Market
    CURRENCY: str = "EUR"
    COUNTRY: str = "ES"
    LANGUAGE: str = "es_ES"

    class Config:
        env_file = ".env"
        case_sensitive = True


# Create global settings instance
settings = Settings()
