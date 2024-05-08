
from data.database import *
from data.weather import *
from data.other import *

from frameworks.settings import Settings


# --- Settings --- #
weather_settings = Settings(
    latitude=LATITUDE,
    longitude=LONGITUDE,
    timezone=TIMEZONE,
    forecast_days=FORECAST_DAYS,
    past_days=PAST_DAYS,
    temperature_unit=TEMPERATURE_UNIT,
    wind_speed_unit=WIND_SPEED_UNIT,
    precipitation_unit=PRECIPITATION_UNIT,
    time_format=TIME_FORMAT,
    models=MODELS
)
