##!/usr/bin/env python3

import time
from appscript import app, mactypes
from applescript import tell

i = 6
x = 30
Crash = 0 
Command2 = 'killall Terminal'
Command1 = 'python3 Documents/Coding/python/crashyassistant.py'
Command = 'python3 Documents/Coding/python/crashy.py'

while x > 0 or Crash > 0:

    def WeLive():
        print("We Live")

    def WeLove():
        print("We Love")

    def WeLie():
        print("We Lie")

    WeLive()
    WeLove()
    WeLie()

    tell.app('Terminal', 'do script "' + Command1 + '"')
    tell.app('Terminal', 'do script "' + Command + '"')
    x -= 1

tell.app('Terminal', 'do script "' + Command2 + '"')
