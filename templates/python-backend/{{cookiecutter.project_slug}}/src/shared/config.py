"""Application configuration using Pydantic settings."""
from typing import List
from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings from environment variables."""
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore",
    )
    
    # Application
    APP_NAME: str = "{{ cookiecutter.project_name }}"
    DEBUG: bool = False
    PORT: int = {{ cookiecutter.port }}
    
    # CORS
    CORS_ORIGINS: List[str] = Field(
        default=["http://localhost:3000", "http://localhost:5173"]
    )
    
    # GraphQL
    ENABLE_GRAPHQL: bool = True
    
    {% if cookiecutter.include_postgres == 'y' %}
    # Database
    DATABASE_URL: str = Field(
        default="postgresql://postgres:postgres@localhost:5432/{{ cookiecutter.project_slug }}"
    )
    {% endif %}
    
    # Security
    SECRET_KEY: str = Field(default="your-secret-key-here-change-in-production")
    
    # Rate limiting
    RATE_LIMIT_ENABLED: bool = True
    RATE_LIMIT_PER_MINUTE: int = 60
    
    # Monitoring
    ENABLE_METRICS: bool = True


@lru_cache
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()


settings = get_settings()