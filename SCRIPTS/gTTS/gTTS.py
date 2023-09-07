from gtts import gTTS
from pygame import mixer
import time

myText = "Hello, my name is Python. Popa pipiska kakashkaaaaaaaaaa XD XD"

obj = gTTS(text=myText, lang='es', slow=False)
# Guardar en el folder audios con nombre popakaka.mp3
obj.save("SCRIPTS/gTTS/audios/popakaka2.mp3")

mixer.init()
mixer.music.load("SCRIPTS/gTTS/audios/popakaka2.mp3")
mixer.music.play()
while mixer.music.get_busy():
    time.sleep(1)