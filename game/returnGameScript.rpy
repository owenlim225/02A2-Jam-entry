# For players who don't know how to read. BRUH
label returnGame:
    $ ranDialogue = renpy.random.choice (
            ['{glitch=1.1}I told you to never come back{/glitch}.', 
            '{glitch=1.1}There\'s no secret ending here{/glitch}.',
            '{glitch=1.1}Why are you so persistent? Quit{/glitch}.',
            '{glitch=1.1}You can only play this once. Quit{/glitch}.',
            '{glitch=1.1}Stop your futile effort. Quit{/glitch}.'])

    scene black
    c "{glitch=1.1}{size=100}Pathetic,[pc_name].{/glitch}"
    c "{glitch=1.1}{size=110}Can't you read the title?{/glitch}"
    c "{glitch=1.1}{size=50}[ranDialogue]{/glitch}"
    call quitGame


# Close the program
label quitGame:
    python:
        renpy.quit(relaunch=False, status=0, save=False)
    return
