import os 

def provideScanDirectory():
    directory = os.getcwd() + "/session/defaultScanDirectory.txt"
    try: 
        f = open(directory,"r", encoding="utf-8")
        scanDirectory = f.read()
        return scanDirectory
    except FileNotFoundError:
        print("Setting up default noteXpads scan directory")
        directory = os.getcwd() + "/session/defaultScanDirectory.txt"
        f = open(directory,"w", encoding="utf-8")
        f.write(f"{directory}")



  