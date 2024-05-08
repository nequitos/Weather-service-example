

from abc import ABC, abstractmethod


class ABSHandler(ABC):
    @abstractmethod
    def __init__(
        self,
        url,
        time_sleep,
        framework,
        repository,
    ):
        self.is_running = abs(bool)

        self._url = abs(url)
        self._time_sleep = abs(time_sleep)
        self._framework = abs(framework)
        self._repository = abs(repository)

        self.__session = None

    @abstractmethod
    async def serve_forever(self):
        pass

    @abstractmethod
    async def __set_session(self):
        pass

    @abstractmethod
    async def __survey_time(self, session):
        pass

