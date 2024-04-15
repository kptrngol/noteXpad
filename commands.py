import sqlite3

# Global variables

close = 1

# sqlite3 variables

con = None
cur = None

def userCommand(): 
    print("Waiting for commands")
    command = input("--> ")
    return command

# Functions for each command

def connectDatabase():
    print("Provide a name for your new noteXpad")
    name = input("noteXpad name: ")
    name = "/home/kpg/Projects/backendRoadmap/notexApp/source/src/" + name
    global con
    con = sqlite3.connect(name)
    global cur
    cur = con.cursor()
    print(f"Creating local database (noteXpad): {name}")


# Program control functions
def performAction(command):
    match command:
        case "e" | "end" | "leave" | "finish" | "close":
            global close
            close = 0
            print("Closing")
            return close
        case "c" | "connect":
            connectDatabase()
        case _:
            print("Try again")




