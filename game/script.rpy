# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("The Dark Lord")

image lord = "character.png"
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

    "Jacksonville"
    "Realm: 6.2"
    "20830ch AD"


    "You are the newly appointed Chief Universal Neuropsychology Technician for the company."

    c "So you are the new guy"
    
    menu:
        c "Do you think you'll last here?"

        "Yes":
            c "HAHAHAHA"

            c "Be thankful I dont have enough chromosomes to send you to the shadow realm"

        "No": 
            c "Impressive, out of everyone in your shoes, youre the only one with a brain."


    # This ends the game.

    return
