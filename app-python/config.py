from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    secret: str = '123'
    
    file_login: str
    file_password: str
    
    ENV_LOGIN: str
    ENV_PASSWORD: str

    DOT_ENV_LOGIN: str
    DOT_ENV_PASSWORD: str

    class Config:
        case_sensitive = True
        secrets_dir = '/run/secrets'


settings = Settings()
