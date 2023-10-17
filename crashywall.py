from applescript import tell
from appscript import app, mactypes
import time

a = 1 
i = 6
command = 'python3 Documents/Coding/python/crashyassistant.py'
command1 = 'python3 Documents/Coding/python/crashy.py'

tell.app('Terminal', 'do script "' + command + '"')

time.sleep(5)

tell.app('Terminal', 'do script "' + command1 + '"')

while a > 0:
    time.sleep(.5)
    app('Finder').desktop_picture.set(mactypes.File('Downloads/shalushai_7.png'))
