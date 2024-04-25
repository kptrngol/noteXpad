import session_manager as sm
import commands as c
import os

# Starting session
defaultScanPath = sm.returnScanPath()
print(f"Scan path: {defaultScanPath}")

while c.close:
    # Listing all notepads from default directory
    # Listing all notes if connected to notepad
    c.performAction(c.userCommand(defaultScanPath),defaultScanPath)