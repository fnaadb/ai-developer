from typing import Annotated
import aiohttp
from semantic_kernel.functions import kernel_function



class WeatherPlugin:
    """A Weather Plugin to get weather data from the Open-Meteo API."""


    @kernel_function(description="Gets the forecast for a given latitude, longitude and number of days. Can forecast up to 16 days in the future..")
    async def get_weather_forecast(self,
                                   latitude: Annotated[str, "The latitude of the location."],
                                   longitude: Annotated[str, "The longitude of the location."],
                                   days: Annotated[int, "Number of days in the future (max 16)."]
                                   ) -> Annotated[dict, "JSON response containing the weather forecast data for the given location and range of days"]:
        
        if days <= 0 or days > 16:
            return {"error": "Day count is out of bounds. Days should be between 1 and 16"}
        
        url = (
            f"https://api.open-meteo.com/v1/forecast"
            f"?latitude={latitude}"
            f"&longitude={longitude}"
            f"&daily=weathercode,temperature_2m_max,temperature_2m_min"
            f"&temperature_unit=fahrenheit"
            f"&forecast_days={days}"
        )
        print(url)

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()  # Raise an error for bad responses
                return await response.json()