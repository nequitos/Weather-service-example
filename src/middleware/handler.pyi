
from src.frameworks.weather import Weather
from src.repositories.weather import WeatherRepository

from aiohttp import ClientSession

from typing import TypeVar, Generic


T = TypeVar("T")

class Handler(Generic[T]):
    def __init__[T: (str, int, Weather, WeatherRepository)](
        self, url: T, survey_delay: T, framework: T, repository: T
    ) -> None:
        self._url = url
        self._survey_delay = survey_delay
        self._framework = framework
        self._repository = repository
        ...
    async def serve_forever(self) -> None: ...
    async def __set_session(self) -> None: ...

    async def __survey_time(self, session: ClientSession) -> None: ...
