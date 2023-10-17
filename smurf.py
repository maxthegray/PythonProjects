#`! /usr/bin/env python3

import time
from appscript import app, mactypes
from applescript import tell
import sys
# import pdb; pdb.set_trace()

def we_live():
	print("We Live")


def we_love():
	print("We Love")


def we_lie():
	print("We Lie")

we_live()
time.sleep(.75)
we_love()
time.sleep(.75)
we_lie()

class SillyClass:
	def __init__(self, run_forever):
		self.run_forever = run_forever

	def get_command(self, num):
		if self.run_forever:
			return 'python3 Documents/Coding/python/smurf.py '

		return 'python3 Documents/Coding/python/smurf.py ' + str(num - 1)


	def maxie_foo(self, num):
		if num > 0 or self.run_forever:
			print("Window #: " + str(num))
			
			tell.app( 'Terminal', 'do script "' + self.get_command(num) + '"')

			self.run_forever

			app('Finder').desktop_picture.set(mactypes.File('Downloads/App Store logo.jpeg'))
			app('Finder').desktop_picture.set(mactypes.File('Downloads/smurf.jpeg'))  
			
				
			we_live()
			time.sleep(.75)
			we_love()
			time.sleep(.75)
			we_lie()
			num += 1
  
		else:
			print("We receoved 0")

def main():
	if len(sys.argv) == 1:
		silly_class = SillyClass(True)
		silly_class.maxie_foo(0)
	else:
		num = int(sys.argv[1])
		silly_class = SillyClass(False)
		silly_class.maxie_foo(num)


if __name__ == "__main__":
	main()
