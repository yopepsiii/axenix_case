from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    team_name: str
    case_api_url: str
    redis_host: str
    redis_port: int

    class Config:
        env_file = ".env"


settings = Settings()

# может сюда уместно Singletone?
