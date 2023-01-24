from functools import lru_cache
from pydantic import BaseSettings

class Config(BaseSettings):
    ACCESS_TOKEN_EXPIRATION: int = 5 * 60 # 5 minutes
    
    PRIVATE_KEY: str
    PUBLIC_KEY: str
    REFRESH_PRIVATE_KEY: str
    
    class Config:
        env_file = '.env'
        

@lru_cache
def get_config():
    return Config()


config = get_config()