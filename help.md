Structure:                              Command     Action

global menu
    create xpad                         :cxp        Creates new SQLite table/notepad
    delete xpad                         :dxp        Deletes SQLite table/notepad
    select xpad (listing xnotes)        :sxp        Selects specific SQLite table/notepad

        sort
        create xnote                    :cxn        Creates new note in the currently selected xpad
        readall xnote                   
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
    help                                :h
    directory                           :dir        Changes default directory for notepads
    import                              :imp
    export                              :exp
    exit                                :e