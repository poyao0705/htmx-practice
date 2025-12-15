from pathlib import Path
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # ../core/config.py -> ../core -> app
    APP_DIR: Path = Path(__file__).resolve().parent.parent
    DB_NAME: str = "database.db"

    @property
    def DATABASE_URL(self) -> str:
        return f"sqlite+aiosqlite:///{self.APP_DIR}/db/{self.DB_NAME}"


settings = Settings()
