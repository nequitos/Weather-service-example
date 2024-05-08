
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Float

from datetime import datetime


class WeatherBase(DeclarativeBase, AsyncAttrs):
    pass


class WeatherORM(WeatherBase):
    __tablename__ = "weather"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True, nullable=False)
    location_name: Mapped[str] = mapped_column(String(50), nullable=False)
    x_coordinate: Mapped[float] = mapped_column(Float, nullable=False)
    y_coordinate: Mapped[float] = mapped_column(Float, nullable=False)
    temperature: Mapped[float] = mapped_column(Float, nullable=True)
    rain: Mapped[float] = mapped_column(Float, nullable=True)
    showers: Mapped[float] = mapped_column(Float, nullable=True)
    snowfall: Mapped[float] = mapped_column(Float, nullable=True)
    surface_pressure: Mapped[float] = mapped_column(Float, nullable=True)
    wind_speed: Mapped[float] = mapped_column(Float, nullable=True)
    wind_direction: Mapped[int] = mapped_column(Float, nullable=True)

    def __repr__(self):
        return f"""
        WeatherORM(
        id={self.id!r}, 
        location_name={self.location_name!r}, 
        x_coordinate={self.x_coordinate!r}, 
        y_coordinate={self.y_coordinate!r}, 
        temperature={self.temperature!r}, 
        rain={self.rain!r}, 
        showers={self.showers!r}, 
        snowfall={self.snowfall!r}, 
        surface_pressure={self.surface_pressure!r}, 
        wind_speed={self.wind_speed!r}, 
        wind_direction={self.wind_direction!r}
        """
