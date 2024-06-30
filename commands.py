import sqlite3
import os
import re
import curses
import curses.textpad
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

def printHelp(defaultScanPath):
    f = open(defaultScanPath + "/help.md","r", encoding="utf-8")
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
                title TEXT NOT NULL,
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
        xnoteTitlesResults = xnoteTitles.fetchall()
        print(f"""
        ------------------------
        Notes from this noteXpad: {xnoteTitlesResults}
        ------------------------
        """)
        return xnoteTitlesResults

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

def editXnote(stdscr):
    stdscr.clear()
    notesToShow = listAllXnotes()
    stdscr.addstr(0,0,f"{notesToShow}")
    stdscr.addstr(1,0,"Select xnote id to edit")
    selectedXnoteId = stdscr.getkey()
    xnotes = cur.execute("SELECT id, title, body FROM xnote")
    
    for xnote in xnotes:
        if selectedXnoteId == str(xnote[0]):
            stdscr.clear()
            selectedXnoteTitle = xnote[1]
            selectedXnoteBody = xnote[2]
            stdscr.addstr(0,0,f"{selectedXnoteTitle} with {selectedXnoteBody}")
            
            # title edit
            stdscr.clear()
            stdscr.addstr(0,0, "Would you like to update the xnote's title?")
            stdscr.addstr(1,0, "yes [y] or no [n]:")
            updateTitle = stdscr.getkey()
            if updateTitle == "y":
                stdscr.clear()
                stdscr.addstr(0,0, "Edit your xnote's title and press Ctrl-G to finish")
                notePad = curses.textpad.Textbox(stdscr)
                notePad.edit()
                selectedXnoteTitle = notePad.gather()

            # xnote body edit
            stdscr.clear()
            stdscr.addstr(0,0, "Would you like to update the xnote's body?")
            stdscr.addstr(1,0, "yes [y] or no [n]:")
            updateBody = stdscr.getkey()
            if updateBody == "y":
                stdscr.clear()
                stdscr.addstr(0,0, "Edit your xnote and press Ctrl-G to finish")
                notePad = curses.textpad.Textbox(stdscr)
                notePad.edit()
                selectedXnoteBody = notePad.gather()

            if (updateBody == "y" or updateTitle == "y"):                    
                cur.execute("""
                UPDATE xnote 
                SET title = :newTitle, body = :updateBody
                WHERE id = :updateId;
                """,{"newTitle" : selectedXnoteTitle, "updateBody" : selectedXnoteBody, "updateId" : selectedXnoteId})
                con.commit()
            
        else:
            print("Please, provide the correct ID")


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
            printHelp(defaultScanPath)
        case "sxp":
            os.system("clear")
            selectXpad(defaultScanPath)
            listAllXnotes()
        case "cxp":
            createXpad(defaultScanPath)
        case "cxn":
            createXnote()
        case "exn":
            wrapper(editXnote)
        case "laxn":
            listAllXnotes()
        case "paxn":
            printAllXnotes()
        case _:
            print("Try again")




