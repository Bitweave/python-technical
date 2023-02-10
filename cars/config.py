from pydantic import BaseSettings


class Settings(BaseSettings):
    AWS_ACCESS_KEY_ID: str = "access-key-id"
    AWS_SECRET_KEY: str = "secret-key"
    LOGGING_LEVEL: str = "INFO"


settings = Settings()
