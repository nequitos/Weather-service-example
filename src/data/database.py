

from environs import Env


env = Env()
env.read_env()

SQL_ALCHEMY_POSTGRES_URL = env.str("SQL_ALCHEMY_POSTGRES_URL")
