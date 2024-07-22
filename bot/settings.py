from pydantic_settings import BaseSettings, SettingsConfigDict

from dotenv import load_dotenv
from yarl import URL

load_dotenv()


class Settings(BaseSettings):

    CB_URL: str = "https://cbr.ru/scripts/XML_daily.asp"

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