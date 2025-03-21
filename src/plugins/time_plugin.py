from typing import TypedDict, Annotated, Optional  
from semantic_kernel.functions import kernel_function
import datetime

class TimePlugin:
    """A Time Plugin to provide date and time-related functions."""

    @kernel_function(description="Returns the current date and time.")
    def get_current_datetime(self) -> Annotated[str, "The current date and time in ISO format."]:
        now = datetime.datetime.now()
        return now.strftime('%Y-%m-%d %H:%M:%S')
    
    @kernel_function(description="Returns the year for a given date.")
    def get_year(self, date: Annotated[str, "The date in ISO format."]) -> Annotated[int, "The year of the given date."]:
        return datetime.datetime.strptime(date, '%Y-%m-%d').year
    
    @kernel_function(description="Returns the month for a given date.")
    def get_month(self, date: Annotated[str, "The date in ISO format."]) -> Annotated[int, "The month of the given date."]:
        return datetime.datetime.strptime(date, '%Y-%m-%d').month

    @kernel_function(description="Returns the day of the week for a given date.")
    def get_day_of_week(self, date: Annotated[str, "The date in ISO format."]) -> Annotated[str, "The day of the week for the given date."]:
        return datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%A')