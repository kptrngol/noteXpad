import sqlite3
import os
import re
import curses
from curses import wrapper

# Global application variables

close = 1

# sqlite3 variables

con = None # Connection global variable
cur = None # Cursor global variable
currentDirectory = os.getcwd()
currentXpad = None

# Main functions

def cursesInit(stdscr):
    stdscr.clear()
    stdscr.refresh()
    stdscr.getch()


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
        print("Closed current Xpad")
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
        xnoteTitles = cur.execute("SELECT id, title FROM xnote")
        print(f"""
        ------------------------
        Notes from this noteXpad: {xnoteTitles.fetchall()}
        ------------------------
        """)
        return xnoteTitles.fetchall()

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

def editXnote():
    print("Select xnote id to edit")
    listAllXnotes()
    selectedXnoteId = input("--> ")

    xnotes = cur.execute("SELECT id, title, body FROM xnote")
    for xnote in xnotes:
        if selectedXnoteId == str(xnote[0]):
            selectedXnoteTitle = xnote[1]
            selectedXnoteBody = xnote[2]
            print(f"Editing {selectedXnoteTitle} with {selectedXnoteBody}")
        else:
            print("Please, provide the correct ID")
    # wrapper(cursesInit)


# Program control functions
def performAction(command,defaultScanPath):
    os.system("clear")
    match command:
        case "e" | "exit":
            closeCurrentXpad()
            print("Closing noteXpad session")
            global close
            close = 0
            return close
        case "h" | "help":
            printHelp()
        case "sxp":
            os.system("clear")
            selectXpad(defaultScanPath)
            listAllXnotes()
        case "cxp":
            createXpad(defaultScanPath)
        case "cxn":
            createXnote()
        case "exn":
            editXnote()
        case "laxn":
            listAllXnotes()
        case "paxn":
            printAllXnotes()
        case _:
            print("Try again")




