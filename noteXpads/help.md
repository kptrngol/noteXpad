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