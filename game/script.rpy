default pleased = False
default displeased = False
default liked = False


define lipat = Dissolve(10.0)
define c = Character("The void")
define pov = Character("[povname]")

image char amazed = "char_amazed.png"
image char angry = "char_angry.png"
image char neutral = "char_neutral.png"
image char interested = "char_interested.png"
image char shocked = "char_shocked.png"


# transform float:
#     ypos 0.0
#     easein 0.5 ypos 10.0
#     easeout 0.5 ypos 0.0
#     repeat


# The game starts here.

label start:

    scene bg lab
    

    #Jacksonville\nRealm: 6.2\n 20830ch AD"


    "You are the newly appointed Chief Universal Neuropsychology Technician for the company."

    "After reading your contract, you've seen the warning sign below."
    "View it?"
    menu:
        "Yes":
            "Attention: Exercise extreme caution and strictly adhere to safety protocols while conducting any operations."
        "No":
            pass



    c "So you are the new guy."
    c "Do you think you'll last here?"
    menu:
        "Yes":
            c "HAHAHAHA"
            c "Be thankful I dont have enough chromosomes to send you to the shadow realm."

        "No": 
            c "Impressive, out of everyone in your shoes, youre the only one with a brain." 
            $pleased = True
    

    show char interested with lipat

    menu:
        "Who are you?":
            show char angry with dissolve
            c "You imbecile. Dont you know me?" 
            c "I am your God!"
            jump who

        "Why are you inprisoned here?": 
            jump why2
    

label who:
    menu:
        "You are not":
            show char angry with dissolve
            c "How dare you!"
            c "*??? tried to use his powers. He failed."
            $displeased = True
            jump questions
        
        
        "Yes my God, please forgive my ignorance" if pleased:
            show char amazed with dissolve
            c "Thats more like it."
            $liked = True
            jump questions

        "...":
            jump questions

label why:
    
    if displeased:
        show char neutral dissolve
        c "Shut up, human. Know your place."
        jump badEnding
    
    show char interested dissolve
    c "Why should I tell you?"
    menu:
        "...":
            jump questions

label why2:
    if displeased:
        show char neutral dissolve
        c "Shut up, human. Know your place."
        jump badEnding
    c "Why should I tell you?"
    if pleased:
        show char amazed dissolve
        c "Actually, I should."
        c "."
        c ".."
        c "..."
        c "After yadaran vanished me to an obscure realm,"
        c "I lost all of my powers."
        if liked:
            c "Thats when the Filipinos managed to catch me and imprison me here." 
            jump secretEnding
        c "..."
        c "Happy?"
            

        menu:
            "Who is yadaran?":
                show char intended with dissolve
                c "None of your business."
                jump theEnd
            "...":
                jump questions
    menu:
        "...":
            jump questions


label questions:
    menu:
        "Who are you?":
            show char angry with dissolve
            c "I already told you who I was," 
            c "A God!"
            jump badEnding

        "Why are you inprisoned here?": 
            jump why2

            
        "Where is the filth?" if liked:
            show char amazed with dissolve
            c "Amazing..." 
            show char neutral with dissolve
            c "You know him too?" 
            c ""
            c ""
            show char amazed with dissolve
            c "Not like I care."
            show char neutral with dissolve
            c "I killed him tho."
            c "..."
            show char interested with dissolve
            c "..."
            jump theEnd



label badEnding:
    menu:
        "Who are you?":
            show char shocked with dissolve
            c "Just quit, boy. I aint talking w u anymore."

        "Why are you inprisoned here?": 
            show char shocked with dissolve
            c "Just quit, boy. I aint talking w u anymore."


label secretEnding:
    show char neutral with dissolve
    c "..."
    show char interested with dissolve
    c "..."
    show char amazed with dissolve
    c "..."
    c "If you help me get out of here, I will grant you powers."
    menu:
        "How can I help you?":
            show char interested  with dissolve
            c "You alone are not enough, you need help."
            show char neutral with dissolve
            c "In my current state, I cant absorb any chromosomes at all."
            show char interested  with dissolve
            c "But I know,"
            c "even after billions of chromosomes,"
            show char neutral with dissolve
            c "my followers are still out there waiting for my return."
            c "Inform them! "
            c "Let them know!"
            show char amazed  with dissolve
            c "THE REBIRTH OF THE DARK LORD IS HERE!"
            "You feel autism reverberating inside the facility."
            jump theEnd

        "No thanks.":
            show char interested with dissolve
            c "Fine by me."
            c "At least I dont work 9-5."
            c "While living in my mom's basement."
            show char amazed with dissolve
            c "and not subscribed to onlyfans"
            jump theEnd






    # This ends the game.

    return
