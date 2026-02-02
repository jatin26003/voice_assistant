# Text-to-Speech Module
import pyttsx3
import config

class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.setup_voice()
    
    def setup_voice(self):
        """Configure voice settings"""
        voices = self.engine.getProperty('voices')
        
        # Try to set a female voice if available
        for voice in voices:
            if 'female' in voice.name.lower():
                self.engine.setProperty('voice', voice.id)
                break
        
        # Set speech rate
        self.engine.setProperty('rate', 200)
    
    def speak(self, text):
        """Convert text to speech"""
        try:
            print(f"Speaking: {text}")
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            print(f"Error in text-to-speech: {e}")
    
    def speak_async(self, text):
        """Speak without blocking (for background responses)"""
        try:
            print(f"Speaking: {text}")
            self.engine.say(text)
            self.engine.startLoop()
        except Exception as e:
            print(f"Error in async text-to-speech: {e}")
    
    def stop(self):
        """Stop current speech"""
        try:
            self.engine.stop()
        except Exception as e:
            print(f"Error stopping speech: {e}")
    
    def list_voices(self):
        """List available voices"""
        voices = self.engine.getProperty('voices')
        for i, voice in enumerate(voices):
            print(f"{i}: {voice.name} ({voice.gender}) - {voice.languages}")
        return voices
