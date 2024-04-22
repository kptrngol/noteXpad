import os 

def returnScanPath():
    scanPathData = os.getcwd() + "/session/defaultScanPath.txt"
    try: 
        f = open(scanPathData,"r", encoding="utf-8")
        scanPath = f.read()
        return scanPath
    except FileNotFoundError:
        print("Setting up default noteXpads scan directory")
        scanPathData = os.getcwd() + "/session/defaultScanPath.txt"
        f = open(scanPathData,"w", encoding="utf-8")
        directory = os.getcwd() + "/noteXpads/"
        f.write(f"{directory}")
    except Exception as error:
        print(f"Error: {error}")



  