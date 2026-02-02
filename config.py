# Configuration for Voice Assistant
import os

# API Keys (set environment variables or replace with your keys)
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY', '')
NEWS_API_KEY = os.getenv('NEWS_API_KEY', '')

# Default city for weather
DEFAULT_CITY = 'New York'

# Speech settings
RECOGNIZER_ENGINE = 'google'  # Options: google, sphinx
TTS_ENGINE = 'sapi5'  # Options: sapi5 (Windows), nsss (macOS), espeak (Linux)

# Reminder settings
REMINDER_STORAGE_FILE = 'reminders.json'

# Assistant settings
WAKE_WORD = 'assistant'
LISTEN_TIMEOUT = 5  # seconds
PHRASE_TIME_LIMIT = 10  # seconds
