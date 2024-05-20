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
    exit                                :e
```


