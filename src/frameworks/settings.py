
from abc import ABC
from src.adapters.settings import ABSSettings


class Settings(dict, ABSSettings):
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
        super().__init__(
            latitude=latitude,
            longitude=longitude,
            timezone=timezone,
            forecast_days=forecast_days,
            past_days=past_days,
            temperature_unit=temperature_unit,
            wind_speed_unit=wind_speed_unit,
            precipitation_unit=precipitation_unit,
            time_format=time_format,
            models=models
        )
        self.__dict__["hourly"] = []

    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __getitem__(self, key):
        return self.__dict__[key]

    def __repr__(self):
        return repr(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __delitem__(self, key):
        del self.__dict__[key]

    def __contains__(self, item):
        return item in self.__dict__

    def __iter__(self):
        return iter(self.__dict__)

    def __add__(self, other):
        self.__dict__["hourly"].append(other)
