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
            
            
    def fetch_current_weather(self, city: str) -> dict:
        url = f"{self.BASE_URL}/weather"
        params = {"q": city, "appid": self.api_key, "units": "metric"}
        data = self._get(url, params)
        
        return {
            "city":          data["name"],
            "country":       data["sys"]["country"],
            "temp":          data["main"]["temp"],
            "feels_like":    data["main"]["feels_like"],
            "humidity":      data["main"]["humidity"],
            "wind_speed":    data["wind"]["speed"],
            "condition":     data["weather"][0]["description"].title(),
        }
        
       
    def fetch_forecast(self, city: str) -> list[dict]:
        url = f"{self.BASE_URL}/forecast"
        params = {"q": city, "appid": self.api_key, "units": "metric"}
        data = self._get(url, params)
        forecast_list: list[dict] = []
        for item in data["list"]:
            if "12:00:00" in item["dt_txt"]:
                date_obj = datetime.strptime(item["dt_txt"], "%Y-%m-%d %H:%M:%S")
                forecast_list.append({
                    "day":       date_obj.strftime("%A"),
                    "temp":      item["main"]["temp"],
                    "condition": item["weather"][0]["description"].title(),
                })
        return forecast_list
            
    def _get(self, url: str, params: dict) -> dict:
        response = requests.get(url, params = params, timeout = 10)
        response.raise_for_status()
        return response.json()
    
         
            
            
        
