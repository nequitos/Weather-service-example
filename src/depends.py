
import asyncio
import logging
import config

from aiohttp import ClientSession
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine

from frameworks.weather import Weather
from repositories.weather import WeatherRepository
from middleware.handler import Handler


# --- Engines --- #
db_engine: AsyncEngine = create_async_engine(
    url=config.SQL_ALCHEMY_POSTGRES_URL
)

# --- Sessions --- #
db_session: AsyncSession = AsyncSession(
    bind=db_engine
)


# --- Frameworks --- #
weather_framework = Weather(config.weather_settings)

# --- Repositories --- #
weather_repository = WeatherRepository(db_session)

# --- Handlers --- #
weather_handler = Handler(config.OPEN_WEATHER_URL, config.SURVEY_DELAY, weather_framework, weather_repository)
