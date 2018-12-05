import os
import sys
from subprocess import Popen, PIPE

def osascript(scpt, args=[]):
     p = Popen(['osascript', '-'] + args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
     stdout, stderr = p.communicate(scpt.encode('utf-8'))
     return stdout, stderr

def opentab(name, wd, cmds):
    commands = '\n'.join(['do script with command "{}" in window 1'.format(a) for a in cmds])
    script = """
    tell application "System Events"
        tell process "Terminal" to keystroke "t" using command down
    end
    tell application "Terminal"
        activate
        do script with command "cd {}" in window 1
        do script "clear" in window 1
        set custom title of window 1 to "{}"
        {}
    end tell
    """
    _stdout, stderr = osascript(script.format(wd, name, commands))
    if stderr:
        sys.stderr.write('Error in Applescript: {}\n'.format(stderr))
