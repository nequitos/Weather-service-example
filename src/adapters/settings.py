
from abc import ABC, abstractmethod


class ABSSettings(ABC):
    @abstractmethod
    def __init__(
            self,
            latitude,
            longitude,
            timezone,
            forecast_days,
            past_days,
            temperature_unit,
            wind_speed_unit,
            precipitation_unit,
            time_format,
            models
    ):
        self.__config = dict(
            latitude=latitude,
            longitude=longitude,
            timezone=timezone,
            hourly=[],
            forecast_days=forecast_days,
            past_days=past_days,
            temperature_unit=temperature_unit,
            wind_speed_unit=wind_speed_unit,
            precipitation_unit=precipitation_unit,
            time_format=time_format,
            models=models
        )

    @abstractmethod
    def __call__(self, *args, **kwargs):
        return self.__config

    @abstractmethod
    def __add__(self, other):
        self.__config["hourly"].append(other)
