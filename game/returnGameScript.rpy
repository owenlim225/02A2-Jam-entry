label returnGame:
    scene black
    show char dead
    c "[pc_name]"
    c "[ranDialogue]"
    call quitGame

label randomReturnDialogue:
    python:
        import random

        # Define the array of possible dialogues
        ranArray = [
            "I told you to never come back.", 
            "There's no secret ending here.",
            "Why are you so persistent? Quit.",
            "You can only play this once. Quit.",
            "Stop your futile effort. Quit."
        ]

        # Select a random dialogue from the array
        ranDialogue = random.choice(ranArray)

        # Jump to the returnGame label with the selected dialogue
        renpy.jump("returnGame", ranDialogue=ranDialogue)



label quitGame:
    python:
        renpy.quit(relaunch=False, status=0, save=False)
    return
