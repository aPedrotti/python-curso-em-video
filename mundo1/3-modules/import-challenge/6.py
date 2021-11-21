#!/usr/bin/python

print('# Ler e reproduzir um arquivo mp3')

import time
from pygame import mixer # pip install pygame

mixer.init()
mixer.music.load("/home/pedrotti/Music/sample.mp3")
mixer.music.play()
while mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(1)