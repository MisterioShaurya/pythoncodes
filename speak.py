import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

# Text to be spoken
text = "Hello, I am your Python assistant. How can I help you today?"

# Speak the text
engine.say(text)

# Wait for the speech to finish
engine.runAndWait()
