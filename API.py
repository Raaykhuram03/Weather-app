import os
from datetime import datetime
import requests


class WeatherAPI:
    BASE_URL = "https://api.openweathermap.org/data/2.5"
    
    def __init__(self) -> None:
        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        if not self.api_key or self.api_key == "your_actual_api_key_here":
            raise ValueError(
                "Configuration Error: OPENWEATHER_API_KEY is missing or "
                "still set to the placeholder value in your .env file."
            )