**noteXpad**

Simple command line note-taking app built in Python with sqlite3 (SQLite local server). 

Dependencies:
Python
sqlite3

MENU STRUCTURE:

```console

Structure:                              Command     Action

global menu
    create xpad                         :cxp        Creates new SQLite table/notepad
    delete xpad                         :dxp        Deletes SQLite table/notepad
    select xpad (listing xnotes)        :sxp        Selects specific SQLite table/notepad
        return
        sort
        create xnote
        read xnote
            previous
            next
        update xnote
            return
            name
            body
            create tag
            read tag
            update tag
            delete tag
        delete xnote
    help
    directory                           :dir        Changes default directory for notepads
    import                              :imp
    export                              :exp
    exit                                :e
```

TO DO (must have):
- nano compatibility
- installer/script for building latest python dependency
- sync options by export, import functions (.db / .csv)
TO DO (optionally)
- backup & online sync funcionality module (using postgresql)

noteXpad functions:
- new noteXpad initialisation creates database template with attributes as: 

ID, CREATE DATE, LAST EDIT DATE, TAGS, TITLE, NOTE

- editing notes updates attribute LAST EDIT DATE
- change name option
- list all notes option
- view next note option