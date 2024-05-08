
from src.adapters.weather import ABSWeather


__all__ = [
    "Weather"
]


class Weather(ABSWeather):
    def __init__(self, settings):
        self._settings = settings

    def get_weather(self, ts, ws, wd):
        params = [
            f"temperature_{ts}m",
            "rain",
            "showers",
            "snowfall",
            "surface_pressure",
            f"wind_speed_{ws}m",
            f"wind_direction_{wd}m"
        ]
        self._settings["hourly"].append(params)

        return self._settings
