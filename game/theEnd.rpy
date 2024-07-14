
label askName:
    show char interested with dissolve 
    c "{glitch=1.1}You entertain me{/glitch}."
    $ povname = renpy.input("Tell me, what's your name{/glitch}?", length=32)

    if povname == "sex":
        show char amazed with dissolve
        c "{glitch=1.1}That's a funny name{/glitch}."
        c "{glitch=1.1}Considering you never experience it yourself{/glitch}."
        jump restartEnding
    elif povname == "gay":
        show char amazed with dissolve
        c "{glitch=1.1}*sigh"
        c "{glitch=1.1}No need to state the obvious{/glitch}."
        c "{glitch=1.1}We all know{/glitch}."
        jump restartEnding
    elif povname == "nigga":
        show char shocked with dissolve
        c "{glitch=1.1}Are you retarted? Do you want to get cancelled{/glitch}?"
        jump restartEnding
    else:
        show char amazed with dissolve
        c "{glitch=1.1}What a beautiful name, Its a pleasure to meet you [povname]{/glitch}."
        show char amazed with dissolve
        hide char amazed with lipat
        c "Look's like your senior is coming."
        c "{glitch=1.1}See you next time,{/glitch}."
        c "{glitch=1.1}[pc_name]{/glitch}."
        call quitGame

    return



