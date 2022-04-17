#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
from playsound import playsound


class Sound():

    def __init__(self, filename) -> None:
        self.filename = filename
        pass

    def play(self):
        playsound(self.filename, False)
        return
