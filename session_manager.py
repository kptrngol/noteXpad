import os 

def returnScanPath():
    scriptPath = os.path.abspath(__file__) 
    scanPathDir = os.path.dirname(scriptPath)
    scanPathData = scanPathDir + "/session/defaultScanPath.txt"
    # print(scanPathDir, scanPathData)
    try: 
        f = open(scanPathData,"r", encoding="utf-8")
        scanPath = f.read()
        return scanPath
    except FileNotFoundError:
        print("Setting up default noteXpads scan directory")
        f = open(scanPathData,"w", encoding="utf-8")
        directory = scanPathDir + "/noteXpads/"
        f.write(f"{directory}")
        f = open(scanPathData,"r", encoding="utf-8")
        scanPath = f.read()
        return scanPath
    except Exception as error:
        print(f"Error: {error}")



  