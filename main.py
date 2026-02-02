# Voice-Activated Personal Assistant
import time
import threading
import re
from datetime import datetime

from speech import SpeechRecognizer
from tts import TextToSpeech
from reminders import ReminderManager
from weather import WeatherService
from news import NewsService

class VoiceAssistant:
    def __init__(self):
        self.speech = SpeechRecognizer()
        self.tts = TextToSpeech()
        self.reminders = ReminderManager()
        self.weather = WeatherService()
        self.news = NewsService()
        
        self.running = False
        self.listening = False
        
        # Start reminder scheduler
        self.reminders.start_scheduler()
        
        # Command patterns
        self.commands = {
            r'weather|forecast': self.handle_weather,
            r'news|headlines': self.handle_news,
            r'remind|reminder': self.handle_reminders,
            r'time|clock': self.handle_time,
            r'help|commands': self.handle_help,
            r'stop|exit|quit': self.handle_stop,
            r'hello|hi|hey': self.handle_greeting
        }
    
    def handle_greeting(self, text):
        """Handle greetings"""
        responses = [
            "Hello! How can I help you today?",
            "Hi there! What can I do for you?",
            "Hey! I'm here to assist you."
        ]
        return random.choice(responses)
    
    def handle_weather(self, text):
        """Handle weather requests"""
        # Extract city name if mentioned
        city_match = re.search(r'in\s+([a-zA-Z\s]+)', text)
        city = city_match.group(1).strip() if city_match else None
        
        if 'forecast' in text:
            return self.weather.get_forecast(city)
        else:
            return self.weather.get_weather(city)
    
    def handle_news(self, text):
        """Handle news requests"""
        # Extract category if mentioned
        category_match = re.search(r'(technology|science|health|business|entertainment|sports)', text)
        category = category_match.group(1) if category_match else None
        
        if 'summary' in text:
            return self.news.get_news_summary()
        elif 'search' in text:
            query_match = re.search(r'search\s+for\s+(.+)', text)
            if query_match:
                return self.news.search_news(query_match.group(1))
            else:
                return "What would you like me to search for?"
        else:
            return self.news.get_headlines(category)
    
    def handle_reminders(self, text):
        """Handle reminder requests"""
        if 'list' in text or 'show' in text:
            return self.reminders.list_reminders()
        
        elif 'delete' in text or 'remove' in text:
            # Extract reminder ID
            id_match = re.search(r'(\d+)', text)
            if id_match:
                return self.reminders.delete_reminder(int(id_match.group(1)))
            else:
                return "Which reminder should I delete? Please provide the reminder number."
        
        else:
            # Extract reminder message and time
            time_match = re.search(r'(\d+)\s+(?:minute|minutes|hour|hours)', text)
            if time_match:
                delay = int(time_match.group(1))
                if 'hour' in text:
                    delay *= 60
                
                # Extract message (everything before the time)
                message_match = re.search(r'remind(?:er)?\s+(.+?)\s+\d+', text)
                if message_match:
                    message = message_match.group(1).strip()
                    return self.reminders.add_reminder(message, delay)
                else:
                    return "What should I remind you about?"
            else:
                return "When should I remind you? Please specify a time."
    
    def handle_time(self, text):
        """Handle time requests"""
        current_time = datetime.now().strftime("%I:%M %p")
        date = datetime.now().strftime("%A, %B %d, %Y")
        return f"The current time is {current_time} on {date}"
    
    def handle_help(self, text):
        """Handle help requests"""
        help_text = """
I can help you with:
- Weather: "What's the weather in London?" or "Weather forecast"
- News: "Get the latest news" or "Technology news"
- Reminders: "Remind me to call mom in 10 minutes"
- Time: "What time is it?"
- Say "stop" or "exit" to quit
        """.strip()
        return help_text
    
    def handle_stop(self, text):
        """Handle stop requests"""
        return "Goodbye!"
    
    def process_command(self, text):
        """Process user command and return response"""
        text = text.lower().strip()
        
        # Check each command pattern
        for pattern, handler in self.commands.items():
            if re.search(pattern, text):
                response = handler(text)
                
                # Check if this is a stop command
                if 'stop' in text or 'exit' in text or 'quit' in text:
                    self.running = False
                
                return response
        
        return "I'm not sure how to help with that. Say 'help' for available commands."
    
    def listen_for_command(self):
        """Listen for a single command"""
        text = self.speech.listen()
        if text:
            return self.process_command(text)
        return None
    
    def run(self):
        """Main assistant loop"""
        self.tts.speak("Voice assistant activated. Say 'assistant' to wake me up.")
        self.running = True
        
        while self.running:
            print("\nWaiting for wake word...")
            
            # Listen continuously for wake word
            while self.running:
                text = self.speech.listen(timeout=1)
                if text and self.speech.is_wake_word(text):
                    self.tts.speak("I'm listening.")
                    break
            
            if not self.running:
                break
            
            # Listen for command after wake word
            response = self.listen_for_command()
            if response:
                self.tts.speak(response)
                
                # If this was a stop command, exit
                if "goodbye" in response.lower():
                    break
            
            time.sleep(0.1)
        
        # Cleanup
        self.reminders.stop_scheduler()
        print("Assistant stopped.")
    
    def start(self):
        """Start the assistant"""
        try:
            self.run()
        except KeyboardInterrupt:
            print("\nAssistant stopped by user.")
            self.reminders.stop_scheduler()
        except Exception as e:
            print(f"Error: {e}")
            self.reminders.stop_scheduler()

if __name__ == "__main__":
    import random
    assistant = VoiceAssistant()
    assistant.start()
