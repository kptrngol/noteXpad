**noteXpad**
---
Simple, offline, command line note-taking app built in Python with sqlite3 (SQLite local server). 

Using only few commands noteXpad allows for fast note creation directly from command line, it was designed for users of tmux-like programs with multiple programs run in one terminal.

**Dependencies**
---

Python 3.11.8,
SQLite version 3.42.0,
curses module (https://docs.python.org/3/library/curses.html#)

Developed and tested on Linux

**Installation**
---
- Install Python, SQLite
- Download all files from this repo into choosen directory
- Edit runxp.sh script (to see the path to paste just use `pwd` command from the script directory):
```
#! /bin/bash
echo 'Running noteXpad'
python PASTE THE PATH
```
- Add this script path at the end of .bashrc or other shell run commands file (usually located in /home/user ) to conveniently access it from different locations
```
export PATH="$HOME/PASTE THE PATH/:$PATH"
```

**Menu**
---

```console

Structure:                              Command     Action

global menu
    create Xpad                         :cxp        Creates new SQLite table/notepad
    delete Xpad                         :dxp        Deletes SQLite table/notepad
    select Xpad (listing xnotes)        :sxp        Selects specific SQLite table/notepad

        create xnote                    :cxn        Creates new note in the currently selected Xpad
        delete xnote
        edit xnote                      :exn        Edit selected xnote
        listall xnotes                  :laxn       List all xnotes from currently selected Xpad
        printall xnotes                 :paxn       Print all xnotes from currently selected Xpad
        
    help                                :h
    directory                           :dir        Changes default directory for notepads
    import                              :imp
    export                              :exp
    exit                                :e
```
**Development notes**
---
TO DO (must have):
- Adding tags management, and time stamps, as using sqlite is justified only by more advanced sorting/categorising features implementation
- installer/script for building python dependency
- sync options by export, import functions (.db / .csv)

TO DO (optionally)
- Possibility to type number representing each noteXpad + also quick selection for xnotes
- backup & online sync funcionality module (using postgresql)
- Commit and close when force exit function
- Handling existing notes to edit them (copying them to temporary file and edit it with nano then commit it to database?)

TO FIX
- Adding name restrictions for Xpad and xnote creation
- Adding longer commands with command + xp / xn name


