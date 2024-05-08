

from sqlalchemy.ext.asyncio import AsyncSession
from src.models.weather import WeatherORM


class WeatherRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def insert(self, scheme):
        data = WeatherORM(
            temperature=scheme.temperature,
            rain=scheme.rain,
            showers=scheme.showers,
            snowfall=scheme.snowfall,
            surface_pressure=scheme.surface_pressure,
            wind_speed=scheme.wind_speed,
            wind_direction=scheme.wind_direction
        )

        async with self._session as session, session.begin():
            session.add(data)

