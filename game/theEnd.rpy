define lipat = Dissolve(10.0)
define c = Character("The void")
define pov = Character("[povname]")

image char amazed = "char_amazed.png"
image char angry = "char_angry.png"
image char neutral = "char_neutral.png"
image char interested = "char_interested.png"
image char shocked = "char_shocked.png"

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
    elif povname == "fnaf":
        c "Wtf is that?"
    elif povname == "sex":
        show char amazed with dissolve
        c "That's a funny name."
        c "Considering you never had it except as your name."
    elif povname == "william afton":
        c "Oh, hes a good friend of mine. Hes as autistic as I am."
    elif povname == "gay":
        show char amazed with dissolve
        c "We all know."
    elif povname == "pink guy":
        show char neutral with dissolve
        c "Thats unlikely."
        c "Out of all lycras, theres only one who can have that name." 
        c "Still, he disappointed me"
        
    elif povname == "red dick":
        show char neutral with dissolve
        c "Thats unlikely."
        c "Out of all lycras, theres only one who can have that name." 
        c "But hes a good fella ngl."
        
    elif povname == "nigga":
        show char shocked with dissolve
        c "Are you retarted? Do you know what year you are in right now?"
    elif povname == "peace lords":
        c "I hate them. Never mention that ever again."
    elif povname == "yadaran":
        c "That damn guy. If it wasnt for him I wouldn't be here in the first place."
    else:
        show char amazed with dissolve
        c "Aight, Its a pleasure to meet you [povname]."

        "Congratulations, your shift is done."
        "You have 15 mins to leave the facility immediately."
        hide char amazed with lipat
        c "See you next time, [povname]."

    return



