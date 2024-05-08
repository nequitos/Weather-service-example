

from environs import Env


env = Env()
env.read_env()

SURVEY_DELAY = env.int("SURVEY_DELAY")
