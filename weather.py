# Weather Module (Stubbed - no API key required)
import random
import config

class WeatherService:
    def __init__(self):
        self.cities = {
            'new york': {'temp': 72, 'condition': 'Partly Cloudy'},
            'london': {'temp': 59, 'condition': 'Rainy'},
            'tokyo': {'temp': 68, 'condition': 'Sunny'},
            'paris': {'temp': 64, 'condition': 'Cloudy'},
            'sydney': {'temp': 77, 'condition': 'Clear'}
        }
    
    def get_weather(self, city=None):
        """Get weather for a city (stubbed data)"""
        city = city.lower() if city else config.DEFAULT_CITY.lower()
        
        # Return stubbed data if city exists, otherwise generate random
        if city in self.cities:
            weather = self.cities[city]
        else:
            weather = {
                'temp': random.randint(50, 85),
                'condition': random.choice(['Sunny', 'Cloudy', 'Rainy', 'Partly Cloudy', 'Clear'])
            }
        
        return f"The weather in {city.title()} is {weather['temp']}°F and {weather['condition']}"
    
    def get_forecast(self, city=None):
        """Get weather forecast (stubbed)"""
        city = city.lower() if city else config.DEFAULT_CITY.lower()
        conditions = ['Sunny', 'Cloudy', 'Rainy', 'Partly Cloudy']
        
        forecast = []
        for day in ['Today', 'Tomorrow', 'Day after']:
            temp = random.randint(50, 85)
            condition = random.choice(conditions)
            forecast.append(f"{day}: {temp}°F, {condition}")
        
        return f"Weather forecast for {city.title()}: {' | '.join(forecast)}"
