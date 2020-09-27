# Wikipedia Text To Audio Program
# Second - what is GTTS library ?
from gtts import gTTS
import os
text = 'Subscribe to Bek Brace channel!'
file = gTTS(text=text, lang='en', slow=False)
file.save('bek.mp3')
os.system('start bek.mp3')
