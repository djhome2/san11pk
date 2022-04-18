#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
from os import path
import subprocess


class Sound():

    def __init__(self, filename) -> None:
        self.filename = filename
        # self.song=AudioSegment.from_wav(self.filename)
        pass

    def play(self):
        subprocess.Popen(['mplayer', self.filename])
        return


if __name__ == "__main__":
    # execute only if run as a script
    sound_folder = path.join(path.dirname(__file__), 'sounds')
    ready = Sound(path.join(sound_folder, 'getready.m4a'))
    ready.play()
