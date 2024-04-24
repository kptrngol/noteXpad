Structure:                              Command     Action

global menu
    create Xpad                         :cxp        Creates new SQLite table/notepad
    delete Xpad                         :dxp        Deletes SQLite table/notepad
    select Xpad (listing xnotes)        :sxp        Selects specific SQLite table/notepad

        create xnote                    :cxn        Creates new note in the currently selected Xpad
        delete xnote
        update xnote
            name
            body
        listall xnote                   :laxn       List all xnotes from currently selected Xpad
        printall xnote                  :paxn       Print all xnotes from currently selected Xpad
        
    help                                :h
    directory                           :dir        Changes default directory for notepads
    import                              :imp
    export                              :exp
    exit                                :e