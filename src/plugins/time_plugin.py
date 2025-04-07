from typing import TypedDict, Annotated, Optional  
from semantic_kernel.functions import kernel_function
import datetime

from app_insights_tracing import get_logger, enable_telemetry
import logging
from opentelemetry import trace


logger = get_logger(__name__)
enable_telemetry(True)
tracer = trace.get_tracer(__name__)


class TimePlugin:
    """A Time Plugin to provide date and time-related functions."""


    @tracer.start_as_current_span(name="time_plugin- get_current_datetime")
    @kernel_function(description="Returns the current date and time.")
    def get_current_datetime(self) -> Annotated[str, "The current date and time in ISO format."]:
        now = datetime.datetime.now()
        return now.strftime('%Y-%m-%d %H:%M:%S')
    
    @tracer.start_as_current_span(name="time_plugin- get_year")
    @kernel_function(description="Returns the year for a given date.")
    def get_year(self, date: Annotated[str, "The date in ISO format."]) -> Annotated[int, "The year of the given date."]:
        return datetime.datetime.strptime(date, '%Y-%m-%d').year
    

    @tracer.start_as_current_span(name="time_plugin- get_month")
    @kernel_function(description="Returns the month for a given date.")
    def get_month(self, date: Annotated[str, "The date in ISO format."]) -> Annotated[int, "The month of the given date."]:
        return datetime.datetime.strptime(date, '%Y-%m-%d').month
    


    @tracer.start_as_current_span(name="time_plugin- get_day_of_week")
    @kernel_function(description="Returns the day of the week for a given date.")
    def get_day_of_week(self, date: Annotated[str, "The date in ISO format."]) -> Annotated[str, "The day of the week for the given date."]:
        return datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%A')