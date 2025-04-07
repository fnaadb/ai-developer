from typing import TypedDict, Annotated, Optional  
import requests  
import asyncio  
from semantic_kernel.functions import kernel_function
import os
from dotenv import load_dotenv

from app_insights_tracing import get_logger, enable_telemetry
import logging
from opentelemetry import trace


logger = get_logger(__name__)
enable_telemetry(True)
tracer = trace.get_tracer(__name__)

class GeoPlugin:

    @tracer.start_as_current_span(name="GeoPlugin")
    @kernel_function(description="Gets the latitude and longitude for a location.")
    async def get_latitude_longitude(self, location:Annotated[str, "The name of the location"]):  
        print(f"lat/long request location: {location}")
        url = f"https://geocode.maps.co/search?q={location}&api_key={os.getenv('GEOCODING_API_KEY')}"  
        response = requests.get(url) 
        data = response.json() 
        position = data[0]
        return f"Latitude: {position['lat']}, Longitude: {position['lon']}"