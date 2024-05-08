
from abc import ABC, abstractmethod


__all__ = [
    "ABSWeather"
]


class ABSWeather(ABC):
    @abstractmethod
    def __init__(
        self,
        settings
    ):
        self._settings = abs(settings)

    @abstractmethod
    async def get_weather(self, ts, ws, wd):
        pass

