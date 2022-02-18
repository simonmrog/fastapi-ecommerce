from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    ENVIRONMENT: str = Field("dev")
    APP_TITLE: str
    APP_DESCRIPTION: str
    APP_VERSION: str
    DATABASE_USERNAME: str = Field("postgres")
    DATABASE_PASSWORD: str = Field("postgres")
    DATABASE_HOST: str
    DATABASE_NAME: str = Field("ecommerce-dev")
    TEST_DATABASE_NAME: str = Field("ecommerce-test")


settings = Settings()
