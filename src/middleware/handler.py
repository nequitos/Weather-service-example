
from src.adapters.handler import ABSHandler
from aiohttp import ClientSession

from asyncio import gather, sleep


class Handler(ABSHandler):
    def __init__(self, url, survey_delay, framework, repository):
        self.is_running = False

        self._url = url
        self._survey_delay = survey_delay
        self._framework = framework
        self._repository = repository

    async def serve_forever(self):
        self.is_running = True
        await self.__set_session()

    async def __set_session(self):
        async with ClientSession(
            base_url=self._url
        ) as session:
            await self.__survey_time(session)

    async def __survey_time(self, session):
        params = self._framework.get_weather(10, 10, 10)
        await session.get(params)
        await self._repository.insert()