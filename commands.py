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


def userCommand(defaultScanPath):
    """
    Prompts user for a command which is passed as an argument to performAction(). This function prints default view between commands in terminal.
    This allows user to move across program's menu. 
    """
    pattern = r"([^/]+\.db)$"
    if currentXpad is None:
        currentXpadResult = "None"
    else:
        currentXpadResult = re.search(pattern,currentXpad).group()

    try:
        print(f"""
        ------------------------
        Waiting for commands
        Available Xpads: {os.listdir(defaultScanPath)}
        Currently selected Xpad: {currentXpadResult}
        ------------------------
        """)
    except Exception:
        print(f"""
        ------------------------
        Waiting for commands
        Currently selected Xpad: None
        ------------------------
        """)
    command = input("--> ")
    return command

# Functions for each command

def closeCurrentXpad():
    try:
        cur.close()
        print("Closed current xnote")
    except AttributeError:
        return
    except Exception as error:
        print(f"Error: {error}")

def printHelp():
    f = open(currentDirectory + "/help.md","r", encoding="utf-8")
    print(f.read())

def selectXpad(defaultScanPath):
    closeCurrentXpad()
    print(f"Select noteXpad file (type full file name) {os.listdir(defaultScanPath)}")
    print(os.listdir(defaultScanPath))
    selectedXpad = input("--> ")
    # Add check for ".db" code
    check = False
    for noteXpad in os.listdir(defaultScanPath):
        if selectedXpad == noteXpad:
            name = defaultScanPath + noteXpad
            print(f"Connecting to: {name}")
            global currentXpad
            currentXpad = name
            global con
            con = sqlite3.connect(name)
            global cur
            cur = con.cursor()
            check = True
    if not check:
        print("There is no such noteXpad in this directory, check the file name spelling")

def createXpad(defaultScanPath):
    # Check if it not exists
    print(f"Name new noteXpad file")
    newXpad = input("--> ")
    name = defaultScanPath + newXpad + ".db"

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

def listAllXnotes():
    # Check for currently selected noteXpad
    if((currentXpad == None)):
        print("First select noteXpad using 'sxp' command")
    else:
        xnoteTitles = cur.execute("SELECT title FROM xnote")
        print(f"""
        ------------------------
        Notes from this noteXpad: {xnoteTitles.fetchall()}
        ------------------------
        """)
        return

def printAllXnotes():
    # Check for currently selected noteXpad
    if((currentXpad == None)):
        print("First select noteXpad using 'sxp' command")
        return
    else:
        xnoteTitles = cur.execute("SELECT title, body FROM xnote")
        for xnote in xnoteTitles.fetchall():
            print(f"""
            ------------------------
            {xnote[0]}
            {xnote[1]}
            ------------------------
            """)



# def selectXnote():
#     # # Check for currently selected noteXpad
#     # if((currentXpad == None)):
#     #     print("First select noteXpad using 'sxp' command")
#     #     return
#     # else:
#     #     print(f"Adding xnote to {currentXpad}")
#     #     # Ask for title 
#     #     print("Name xnote")
#     #     xnoteName = input("--> ")
#     #     # Ask for content
#     #     print("Write xnote")
#     #     xnoteBody = input("--> ")
#     #     try:
#     #         cur.execute("""
#     #         INSERT INTO xnote (title, body)
#     #         VALUES(:xnoteName, :xnoteBody);
#     #         """,{"xnoteName": xnoteName, "xnoteBody": xnoteBody})
#     #         con.commit()
#     #     except Exception as error:
#     #         print(f"Error: {error}")

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
            INSERT INTO xnote (title, body)
            VALUES(:xnoteName, :xnoteBody);
            """,{"xnoteName": xnoteName, "xnoteBody": xnoteBody})
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
        case "h" | "help":
            printHelp()
        case "sxp":
            selectXpad(defaultScanPath)
            listAllXnotes()
        case "cxp":
            createXpad(defaultScanPath)
        case "sxn":
            selectXnote()
        case "cxn":
            createXnote()
        case "laxn":
            listAllXnotes()
        case "paxn":
            printAllXnotes()
        case _:
            print("Try again")




