#Text to Speech (TTS) library for Python 2 and 3. Works without internet connection or delay.

import pyttsx3
engine = pyttsx3.init()
engine.say("Hey, how are you ?")
engine.runAndWait()
