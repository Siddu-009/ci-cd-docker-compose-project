from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    POSTGRES_USER: str = "admin"

    POSTGRES_PASSWORD: str = "admin123"

    POSTGRES_DB: str = "cicd_db"

    DB_HOST: str = "localhost"

    DB_PORT: int = 5432

    class Config:
        env_file = ".env"


settings = Settings()