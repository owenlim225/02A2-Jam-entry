
label askName:
    show char interested with dissolve 
    c "You entertain me."
    $ povname = renpy.input("Tell me, what's your name?", length=32)

    if povname == "sex":
        show char amazed with dissolve
        c "That's a funny name."
        c "Considering you never experience it yourself."
    elif povname == "gay":
        show char amazed with dissolve
        c "We all know."
    elif povname == "nigga":
        show char shocked with dissolve
        c "Are you retarted? Don't you want to get cancelled?"
    else:
        show char amazed with dissolve
        c "Aight, Its a pleasure to meet you [povname]."
        show char amazed with dissolve
        hide char amazed with lipat
        c "See you next time, [pc_name]."
        call quitGame

    return



