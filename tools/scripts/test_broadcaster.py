#! /usr/bin/env python3.8
# -*- coding: utf-8 -*-

import os
from playsound import playsound

voice_liberary = "/home/yan/下载/"
print("Ready!")
playsound(os.path.join(voice_liberary, "cheer_up.wav"))
print("Finished!")
