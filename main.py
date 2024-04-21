import commands as c
import session_manager as sm
import os

while c.close:
    sm.provideScanDirectory()
    # if it is the first session create default dir and guide to create dir if not use default
    # list all notepads from default directory
    print(os.listdir(c.currentDirectory))
    c.performAction(c.userCommand())