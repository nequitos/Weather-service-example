
from . settings import Settings
from aiohttp import ClientSession
from typing import TypeVar, Generic, Any


__all__ = [
    "Weather"
]


T = TypeVar("T")


class Weather(Generic[T]):
    def __init__(self, settings: Settings) -> None:
        self._settings = settings
        ...
    async def get_weather(self, ts: T, ws: T, wd: T) -> T: ...