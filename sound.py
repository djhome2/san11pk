#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
from playsound import playsound
import winsound
# from pydub.playback import play


class Sound():

    def __init__(self, filename) -> None:
        self.filename = filename
        # self.song=AudioSegment.from_wav(self.filename)
        pass

    def play(self):
        winsound.PlaySound(self.filename, winsound.SND_FILENAME)
        return
