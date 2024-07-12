
label theEnd:
    show char interested with dissolve 
    c "You entertain me."
    $ povname = renpy.input("Tell me, what's your name?", length=32)

    if povname == "frank":
        show char neutral with dissolve
        c "Too damn filthy."
    elif povname == "francis":
        show char interested with dissolve
        c "Oh thats a good name. It reminds me of someone I buried in an interdimensional hole."
    elif povname == "sex":
        show char amazed with dissolve
        c "That's a funny name."
        c "Considering you never experience it yourself."
    elif povname == "gay":
        show char amazed with dissolve
        c "We all know."
    elif povname == "pink guy" or povname == "red dick":
        show char neutral with dissolve
        c "Out of everyone, theres only one lycra who can have that name." 
        c "And that's not you."
    elif povname == "nigga":
        show char shocked with dissolve
        c "Are you retarted? Don't you want to get cancelled?"
    elif povname == "peace lords" or povname == "yadaran":
        show char angry with dissolve
        c "I hate them. Never mention that ever again."
    else:
        show char amazed with dissolve
        c "Aight, Its a pleasure to meet you [povname]."

        "Congratulations, your shift is done."
        "You have 15 mins to leave the facility immediately."
        show char amazed with dissolve
        hide char amazed with lipat
        c "See you next time, [povname]."

    return



