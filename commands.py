import sqlite3
import os
import re

# Global application variables

close = 1

# sqlite3 variables

con = None # Connection global variable
cur = None # Cursor global variable
currentDirectory = os.getcwd()
currentXpad = None

def userCommand():
    """
    Prompts user for a command which is passed as an argument to performAction().
    This allows user to move across program's menu. 
    """
    pattern = r"([^/]+\.db)$" 
    try:
        print(f"""
        ------------------------
        Waiting for commands
        Currently selected xpad: {(re.search(pattern,currentXpad)).group()}
        ------------------------
        """)
    except Exception:
        print(f"""
        ------------------------
        Waiting for commands
        Currently selected xpad: None
        ------------------------
        """)
    command = input("--> ")
    return command

def closeCurrentXpad():
    try:
        cur.close()
        print("Closed current xnote")
    except AttributeError:
        return
    except Exception as error:
        print(f"Error: {error}")

# Functions for each command
def selectXpad(defaultScanPath):
    closeCurrentXpad()
    print(f"Select noteXpad file {os.listdir(defaultScanPath)}")
    print(os.listdir(defaultScanPath))
    selectedXpad = input("--> ")
    # Check
    for noteXpad in os.listdir(defaultScanPath):
        if (selectedXpad == noteXpad):
            name = defaultScanPath + noteXpad
            print(f"Connecting to: {name}")
            global currentXpad
            currentXpad = name
            global con
            con = sqlite3.connect(name)
            global cur
            cur = con.cursor()
        else:
            print("There is no such noteXpad in this directory, check the file name spelling")
            return False

def printHelp():
    f = open(currentDirectory + "/help.md","r", encoding="utf-8")
    print(f.read())
    
def createXpad(defaultScanPath):
    # Check if it not exists
    print(f"Name new noteXpad file")
    newXpad = input("--> ")
    name = defaultScanPath + newXpad

    print(f"Connect to {name}?")
    response = input("yes [y] or no [n]:")
    if (not (response == "y")):
        return
    else:
        closeCurrentXpad()
        print(f"Connecting to: {name}")
        global currentXpad
        currentXpad = name
        global con
        con = sqlite3.connect(name)
        global cur
        cur = con.cursor()
        try: 
            cur.execute("""
            CREATE TABLE IF NOT EXISTS xnote (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL UNIQUE,
                body TEXT);
            """)
            con.commit()
        except Exception as error:
            print(f"Error: {error}")

def selectXnote():
    return

def createXnote():
    # Check for currently selected noteXpad
    if((currentXpad == None)):
        print("First select noteXpad using 'sxp' command")
        return
    else:
        print(f"Adding xnote to {currentXpad}")
        # Ask for title 
        print("Name xnote")
        xnoteName = input("--> ")
        # Ask for content
        print("Write xnote")
        xnoteBody = input("--> ")
        try:
            cur.execute("""
            INSERT INTO :xPadName (title, body)
            VALUES(:xnoteName, :xnoteBody);
            """,{"xPadName": currentXpad, "xnoteName": xnoteName, "xnoteBody": xnoteBody})
            con.commit()
        except Exception as error:
            print(f"Error: {error}")


# Program control functions
def performAction(command,defaultScanPath):
    match command:
        case "e" | "exit":
            closeCurrentXpad()
            global close
            close = 0
            return close
        case "sxp":
            selectXpad(defaultScanPath)
        case "cxp":
            createXpad(defaultScanPath)
        case "sxn":
            selectXnote()
        case "cxn":
            createXnote()
        case "h" | "help":
            printHelp()
        case _:
            print("Try again")




