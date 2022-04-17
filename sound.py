#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
from os import path
from playsound import playsound
import winsound
# from pydub.playback import play
import os
# import play_mp3

class Sound():

    def __init__(self, filename) -> None:
        self.filename = filename
        # self.song=AudioSegment.from_wav(self.filename)
        pass

    def play(self):
        playsound(self.filename)
        return


if __name__ == "__main__":
    # execute only if run as a script
    sound_folder = path.join(path.dirname(__file__), 'sounds')
    ready = Sound(path.join(sound_folder, 'getready.m4a'))
    ready.play()
