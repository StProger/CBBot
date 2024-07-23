from pydantic_settings import BaseSettings, SettingsConfigDict

from dotenv import load_dotenv
from yarl import URL

import os

from apscheduler.schedulers.asyncio import AsyncIOScheduler

load_dotenv()


class Settings(BaseSettings):

    BOT_TIMEZONE: str = "Europe/Moscow"
    BOT_TOKEN: str = os.getenv("BOT_TOKEN").strip()

    # Путь к логам
    PATH_LOGS: str = "bot/data/logs.log"

    CB_URL: str = "https://cbr.ru/scripts/XML_daily.asp"

    FSM_REDIS_HOST: str = os.getenv("FSM_REDIS_HOST").strip()
    FSM_REDIS_DB: int = os.getenv("FSM_REDIS_DB").strip()

    REDIS_HOST: str = os.getenv("REDIS_HOST").strip()
    REDIS_DB: int = os.getenv("REDIS_DB").strip()

    model_config = SettingsConfigDict(env_file="../.env")

    @property
    def fsm_redis_url(self) -> str:
        """
        создание URL для подключения к редису

        :return: redis connection url
        """
        return str(URL.build(
            scheme="redis",
            host=self.FSM_REDIS_HOST,
            path="/" + str(self.FSM_REDIS_DB)
        ))


settings = Settings()
BOT_SCHEDULER = AsyncIOScheduler(timezone=settings.BOT_TIMEZONE)