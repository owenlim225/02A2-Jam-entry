# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("The dark lord")
image lord = "character.png"


default pleased = False
default displeased = False

default liked = False

default Ending = False




# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg lab

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show lord

    # These display lines of dialogue.

    "Jacksonville\nRealm: 6.2\n 20830ch AD"


    "You are the newly appointed Chief Universal Neuropsychology Technician for the company."

    c "So you are the new guy"
    
    menu:
        c "Do you think you'll last here?"

        "Yes":
            c "HAHAHAHA"

            c "Be thankful I dont have enough chromosomes to send you to the shadow realm"

        "No": 
            c "Impressive, out of everyone in your shoes, youre the only one with a brain." 

    
    menu:
        "Who are you?":
            c "You imbecile. Dont you know me? I am your God!"
            jump who

        "Why are you inprisoned here?": 
            jump why
    
    jump questions

label questions:
    menu:
        "Why are you inprisoned here?": 
            jump why
        
        "Where is the filth?" if pleased:
            c "I killed him."
            jump questions



label who:
    menu:
        "You are not":
            c "How dare you!"
            c "*??? tried to use his powers. He failed."
            $displeased = True
            jump questions
        
        "Yes my God, please forgive my ignorance":
            c "That’s more like it."
            $pleased = True
            jump questions

        "...":
            jump questions

label why:
    c "..."
    if pleased:
        c "After yadaran vanished me to an obscure realm,"
        c "I lost all of my powers."
        if liked:
            c "Thats when the Filipinos managed to catch me and imprison me here." 
        c "Happy?"
        jump questions
    if displeased:
        c "Shut up, human. Know your place."
        jump questions






    # This ends the game.

    return
