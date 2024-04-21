import sqlite3
import os

# Global application variables

close = 1

# sqlite3 variables

con = None
cur = None
currentDirectory = os.getcwd()

def userCommand(): 
    print("Waiting for commands")
    command = input("--> ")
    return command

# Functions for each command

# Saving global variables for next sessions in a table 

def selectXpad():

    print("Provide a directory address for new noteXpad instance\nType 'default' for default script working directory\nType specific address for custom working directory")
    addresType = input("--> ")
    global currentDirectory 
    if (addressType == "default"):
        currentDirectory = os.getcwd()  
    else:
        currentDirectory = addressType
    print("Provide a name for your new noteXpad instance")
    name = input("noteXpad name: ")
    name = currentDirectory + "/" + name
    global con
    con = sqlite3.connect(name)
    global cur
    cur = con.cursor()
    print(f"Creating noteXpad instance: {name}")


# Program control functions
def performAction(command):
    match command:
        case "e" | "end" | "leave" | "finish" | "close":
            global close
            close = 0
            print("Closing")
            return close
        case "c" | "connect":
            selectXpad()
        case _:
            print("Try again")




