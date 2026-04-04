from functools import cached_property

from pydantic import Field, AliasGenerator
from pydantic.alias_generators import to_snake
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL


class PostgresDatabaseSettings(BaseSettings):
    USER: str = Field(default="postgres")
    PASSWORD: str = Field(default="password")
    HOST: str = Field(default="localhost")
    PORT: int = Field(5432)
    DB: str = Field("minikube")

    model_config = SettingsConfigDict(
        env_prefix="POSTGRES_",
        alias_generator=AliasGenerator(
            serialization_alias=lambda field: "postgres_" + to_snake(field),
        ),
    )

    @cached_property
    def database_url(self):
        return URL.create(
            drivername="postgresql+psycopg",
            username=self.USER,
            password=self.PASSWORD,
            host=self.HOST,
            port=self.PORT,
            database=self.DB,
        )


postgres_database_settings = PostgresDatabaseSettings()
