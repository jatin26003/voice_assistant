# Voice-Activated Personal Assistant

A Python-based voice assistant that performs tasks like setting reminders, checking weather, and reading news using speech recognition and text-to-speech.

## Features

- **Speech Recognition**: Listen for voice commands using microphone
- **Text-to-Speech**: Respond with spoken feedback
- **Weather Information**: Get current weather and forecasts (stubbed data)
- **News Headlines**: Read latest news by category (stubbed data)
- **Reminder System**: Set and manage timed reminders
- **Wake Word Detection**: Activates when you say "assistant"

## Installation

1. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the assistant:
```bash
python main.py
```

2. Say "assistant" to wake up the assistant
3. Speak your command

## Voice Commands

### Weather
- "What's the weather?"
- "Weather forecast"
- "What's the weather in London?"

### News
- "Get the latest news"
- "Technology news"
- "Search news for technology"

### Reminders
- "Remind me to call mom in 10 minutes"
- "Remind me to take medicine in 1 hour"
- "List my reminders"
- "Delete reminder 1"

### Other
- "What time is it?"
- "Help" (shows available commands)
- "Stop" or "Exit" (quits the assistant)

## Configuration

Edit `config.py` to customize:
- Wake word
- Speech recognition engine
- Text-to-speech engine
- Default city for weather
- API keys (for real weather/news data)

## API Integration (Optional)

To use real weather and news data instead of stubbed data:

1. Get API keys:
   - Weather: OpenWeatherMap (free tier available)
   - News: NewsAPI.org (free tier available)

2. Set environment variables:
```bash
export WEATHER_API_KEY="your_openweather_key"
export NEWS_API_KEY="your_newsapi_key"
```

3. Replace stubbed modules with real API implementations

## Troubleshooting

### Microphone Issues
- Ensure microphone permissions are granted
- Check that microphone is not muted
- Try different microphone if available

### Speech Recognition Issues
- Speak clearly and at moderate pace
- Reduce background noise
- Try different recognition engine in config.py

### Text-to-Speech Issues
- Windows: Uses SAPI5 (built-in)
- macOS: Uses NSSpeechSynthesizer (built-in)
- Linux: May need to install espeak: `sudo apt-get install espeak`

## Project Structure

```
voice_assistant/
├── main.py          # Main assistant loop
├── speech.py        # Speech recognition
├── tts.py           # Text-to-speech
├── reminders.py     # Reminder management
├── weather.py       # Weather service (stubbed)
├── news.py          # News service (stubbed)
├── config.py        # Configuration settings
├── requirements.txt # Python dependencies
└── README.md        # This file
```

## Dependencies

- `SpeechRecognition`: Speech recognition library
- `pyttsx3`: Text-to-speech library
- `pyaudio`: Microphone access
- `schedule`: Task scheduling for reminders
- `requests`: HTTP requests (for future API integration)
- `python-dateutil`: Date/time utilities
- `beautifulsoup4`: Web scraping (for news)
- `lxml`: XML parser

## License

This project is for educational purposes. Feel free to modify and extend it.
