# Speech Recognition Module (Fallback without PyAudio)
import speech_recognition as sr
import config

class SpeechRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = None
        
        # Try to initialize microphone
        try:
            self.microphone = sr.Microphone()
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source)
            print("Microphone initialized successfully")
        except Exception as e:
            print(f"Microphone initialization failed: {e}")
            print("Speech recognition will use file input instead")
    
    def listen(self, timeout=None):
        """Listen for audio and return text"""
        if not self.microphone:
            return self._fallback_input()
        
        try:
            with self.microphone as source:
                print("Listening...")
                audio = self.recognizer.listen(
                    source, 
                    timeout=timeout or config.LISTEN_TIMEOUT,
                    phrase_time_limit=config.PHRASE_TIME_LIMIT
                )
            
            print("Recognizing...")
            if config.RECOGNIZER_ENGINE == 'google':
                text = self.recognizer.recognize_google(audio)
            elif config.RECOGNIZER_ENGINE == 'sphinx':
                text = self.recognizer.recognize_sphinx(audio)
            else:
                text = self.recognizer.recognize_google(audio)  # fallback
            
            print(f"You said: {text}")
            return text.lower()
            
        except sr.WaitTimeoutError:
            print("Listening timed out")
            return ""
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return ""
        except Exception as e:
            print(f"Error in speech recognition: {e}")
            return ""
    
    def _fallback_input(self):
        """Fallback to text input when microphone is not available"""
        print("Microphone not available. Type your command:")
        try:
            text = input("> ")
            print(f"You typed: {text}")
            return text.lower()
        except KeyboardInterrupt:
            return ""
        except Exception as e:
            print(f"Error reading input: {e}")
            return ""
    
    def is_wake_word(self, text):
        """Check if wake word is present"""
        return config.WAKE_WORD in text.lower()
