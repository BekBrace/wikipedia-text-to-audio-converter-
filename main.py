import os
import wikipedia
from gtts import gTTS
wikipedia.set_lang('en')
result = wikipedia.summary('Samurai', sentences=4)
print(result)
# Conversion from text to mp3
myobj = gTTS(text=result, lang="en", slow=False)
myobj.save('samurai.mp3')
os.system('start samurai.mp3')
