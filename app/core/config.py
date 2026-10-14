import os

from dotenv import load_dotenv


# Load local development settings while allowing deployment environment variables
# to take precedence.
load_dotenv()


class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./clients.db")
    SECRET_KEY = os.getenv("SECRET_KEY", "")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30")
    )
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"

    def __init__(self) -> None:
        if not self.SECRET_KEY:
            raise RuntimeError("SECRET_KEY must be set in the environment or .env")
        if self.ACCESS_TOKEN_EXPIRE_MINUTES <= 0:
            raise RuntimeError("ACCESS_TOKEN_EXPIRE_MINUTES must be positive")


settings = Settings()
