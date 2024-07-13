label returnGame:
    $ ranDialogue = renpy.random.choice (
            ['I told you to never come back.', 
            'There\'s no secret ending here.',
            'Why are you so persistent? Quit.',
            'You can only play this once. Quit.',
            'Stop your futile effort. Quit.'])

    scene black
    show char dead
    c "[pc_name]"
    c "[ranDialogue]"
    call quitGame




label quitGame:
    python:
        renpy.quit(relaunch=False, status=0, save=False)
    return
