import sqlite3
import os
import re

# Global application variables

close = 1

# sqlite3 variables

con = None
cur = None
currentDirectory = os.getcwd()
currentXpad = None

def userCommand(): 
    pattern = r"([^/]+\.db)$" 
    try:
        print(f"Waiting for commands\nCurrently selected xpad: {(re.search(pattern,currentXpad)).group()}")
    except Exception:
        print(f"Waiting for commands\nCurrently selected xpad: None")
    command = input("--> ")
    return command

# Functions for each command
def selectXpad(defaultScanPath):
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
    print(f"Name new noteXpad file")
    newXpad = input("--> ")
    name = defaultScanPath + newXpad

    print(f"Connect to {name}?")
    response = input("yes [y] or no [n]:")
    if (not (response == "y")):
        return
    else:
        print(f"Connecting to: {name}")
        global currentXpad
        currentXpad = name
        global con
        con = sqlite3.connect(name)
        global cur
        cur = con.cursor()

# Program control functions
def performAction(command,defaultScanPath):
    match command:
        case "e" | "exit":
            global close
            close = 0
            print("Closing")
            return close
        case "sxp":
            selectXpad(defaultScanPath)
        case "cxp":
            createXpad(defaultScanPath)
        case "h" | "help":
            printHelp()
        case _:
            print("Try again")




