**noteXpad**

Simple command line note-taking app built in Python with SQLite local server. 

MENU STRUCTURE:

```console

Structure:                                    Command

global menu
    create xpad                               :cxp
    delete xpad                               :dxp
    select xpad (listing xnotes)              :sxp
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
    import
    export
    exit
```

TO DO (global app ideas):
- installer/script for building latest python dependency
- sync options by export, import functions
- nano compatibility

TO DO (noteXpad functions):
- new noteXpad initialisation creates database template with attributes as: ID, CREATE DATE, LAST EDIT DATE, TAGS, TITLE, NOTE
- editing notes updates attribute LAST EDIT DATE
- change name option
- list all notes option
- view next note option