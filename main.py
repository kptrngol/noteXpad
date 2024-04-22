import session_manager as sm
import commands as c
import os

# Starting session
defaultScanPath = sm.returnScanPath()
print(f"Scan path: {defaultScanPath}")
print(os.listdir(defaultScanPath))

while c.close:
    # Listing all notepads from default directory
    c.performAction(c.userCommand(),defaultScanPath)