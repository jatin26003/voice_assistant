# Voice Assistant Setup Guide

## Installation Complete! ✅

The voice assistant has been successfully installed and tested.

## Current Status
- ✅ Text-to-Speech working
- ✅ Weather service (stubbed data)
- ✅ News service (stubbed data) 
- ✅ Reminder system working
- ⚠️ Microphone not available (using text input fallback)

## How to Run

### Option 1: Interactive Mode
```bash
cd voice_assistant
python main.py
```
Then type commands like:
- "assistant" (to wake up)
- "what's the weather"
- "get the news"
- "remind me to call mom in 5 minutes"
- "what time is it"
- "stop" (to exit)

### Option 2: Test Mode
```bash
python test_assistant.py
```

## Voice Commands Available
- **Weather**: "what's the weather", "weather in London"
- **News**: "get the news", "technology news"
- **Reminders**: "remind me to [task] in [X] minutes"
- **Time**: "what time is it"
- **Help**: "help" or "commands"
- **Exit**: "stop" or "exit"

## Microphone Setup (Optional)

To enable voice input instead of text input:

1. Install Microsoft Visual C++ Build Tools:
   - Download from: https://visualstudio.microsoft.com/visual-cpp-build-tools/
   - Select "C++ build tools" during installation

2. Install PyAudio:
   ```bash
   pip install pyaudio
   ```

3. Update main.py to use `speech.py` instead of `speech_no_pyaudio.py`:
   ```python
   from speech import SpeechRecognizer  # Change this line
   ```

## Configuration

Edit `config.py` to customize:
- Wake word (default: "assistant")
- Speech recognition engine
- Text-to-speech engine
- Default city for weather

## Next Steps

1. Try the assistant: `python main.py`
2. Test different commands
3. Set up microphone for voice input (optional)
4. Add real API keys for weather/news (optional)

## Troubleshooting

- **TTS not working**: Check system audio settings
- **Microphone issues**: Install PyAudio (see above)
- **Permissions**: Ensure microphone access is allowed
- **Dependencies**: Run `pip install -r requirements_no_pyaudio.txt`

The assistant is ready to use! 🎉
