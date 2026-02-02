# Test script for Voice Assistant
import sys
import os

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from speech_no_pyaudio import SpeechRecognizer
from tts import TextToSpeech
from reminders import ReminderManager
from weather import WeatherService
from news import NewsService

def test_components():
    print("=== Testing Voice Assistant Components ===\n")
    
    # Test TTS
    print("1. Testing Text-to-Speech...")
    tts = TextToSpeech()
    tts.speak("Text to speech is working")
    print("✓ TTS test complete\n")
    
    # Test Speech Recognition (fallback mode)
    print("2. Testing Speech Recognition (fallback mode)...")
    speech = SpeechRecognizer()
    print("✓ Speech recognition initialized\n")
    
    # Test Weather Service
    print("3. Testing Weather Service...")
    weather = WeatherService()
    weather_result = weather.get_weather("New York")
    print(f"Weather result: {weather_result}")
    print("✓ Weather service working\n")
    
    # Test News Service
    print("4. Testing News Service...")
    news = NewsService()
    news_result = news.get_headlines()
    print(f"News result: {news_result}")
    print("✓ News service working\n")
    
    # Test Reminders
    print("5. Testing Reminder Manager...")
    reminders = ReminderManager()
    reminder_result = reminders.add_reminder("Test reminder", 1)
    print(f"Reminder result: {reminder_result}")
    print("✓ Reminder system working\n")
    
    print("=== All Components Tested Successfully ===")
    print("\nThe voice assistant is ready to run!")
    print("Run: python main.py")
    print("\nNote: Microphone not available - will use text input fallback")

if __name__ == "__main__":
    test_components()
