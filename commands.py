import sqlite3

# Global variables
close = 1

def userCommand(): 
    print("Waiting for commands")
    command = input("--> ")
    return command

# Functions for each command

def connectDatabase():
    print("Provide database name")
    name = input("database name: ")
    name = "/home/kpg/Projects/backendRoadmap/notexApp/source/src/" + name
    print(name)
    connect = sqlite3.connect(name)
    print(f"Creating local database {name}")


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




