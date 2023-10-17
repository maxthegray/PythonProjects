#! /usr/bin/env python3

import time
from appscript import app, mactypes
from applescript import tell
# import pdb; pdb.set_trace()

Command = 'python3 Documents/Coding/python/smurf.py'
while True:
	def WeLive():
		print("We Live")
	def WeLove():
		print("We Love")
	def WeLie():
		print("We Lie")

	tell.app( 'Terminal', 'do script "' + Command + '"')

	WeLive()
	time.sleep(.75)
	WeLove()
	time.sleep(.75)
	WeLie()

	app('Finder').desktop_picture.set(mactypes.File('Downloads/smurf.jpeg')) 
