
default pleased = False
default displeased = False
default liked = False
default persistent.game_played = False

define lipat = Dissolve(5.0)
define c = Character("The void")
define pov = Character("[povname]")

image char amazed = "char_amazed.png"
image char angry = "char_angry.png"
image char neutral = "char_neutral.png"
image char interested = "char_interested.png"
image char shocked = "char_shocked.png"
image char dead = "char_dead.png"



label start:

    "Jacksonville\nRealm: 6.2\n20830ch AD"

    scene bg lab with fade
    
    if not persistent.game_played:
        $ persistent.game_played = True
        "You are the newly appointed Chief Universal Neuropsychology Technician for the company."
        "After reading your contract, you've seen the warning sign below."
        "View it?"
        menu:
            "Yes":
                "Attention: Exercise extreme caution and strictly adhere to safety protocols while conducting any operations."
                jump beginning
            "No":
                jump beginning
    else:
        "After reading your contract once again, you don't feel like reading anymore."
        jump beginning






label beginning:
    c "Hello, new guy."
    c "Do you think you'll last here?"
    menu:
        "Yes":
            c "HAHAHAHA"
            c "Be thankful I dont have enough chromosomes to send you to the shadow realm."

        "No": 
            c "Impressive, out of everyone in your shoes, you're the only one with a brain." 
            $pleased = True
    

    show char interested with lipat

    menu:
        "Who are you?":
            show char interested with dissolve
            c "You imbecile. Can't you recognize me?" 
            show char amazed with dissolve
            c "I am a God!"
            jump who

        "Why are you inprisoned here?": 
            jump why2
    

label who:
    menu:
        "You are not":
            show char shocked with dissolve
            c "You dare..."
            show char neutral with dissolve
            c "Well,"
            show char amazed with dissolve
            c "At least I don't work 9-5 job like you."
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
        show char neutral with dissolve
        c "Shut up, boy. Know your place."
        jump badEnding
    
    show char interested with dissolve
    c "Why should I tell you?"
    menu:
        "...":
            jump questions

label why2:
    if displeased:
        show char neutral with dissolve
        c "Shut up, human. Know your place."
        jump badEnding
    c "Why should I tell you?"
    if pleased:
        show char amazed with dissolve
        c "."
        c ".."
        c "..."
        c "Actually,"
        if persistent.game_played == True:
            c "It was after yadaran vanished me to an obscure realm,"
            c "I lost all of my powers."
            c "Thats when the Filipinos managed to catch me and imprison me here." 
            jump secretEnding
        else:
            c "Why do you even care?"
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
            c "A God."
            jump badEnding

        "Why are you inprisoned here?": 
            jump why2

            
        "Where is the filth?" if liked:
            if not persistent.game_played:
                c "You are the only filth here."
                jump theEnd
            else:
                $ persistent.game_played = True
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
                show char dead with dissolve
                scene black with fade
                c "shoud I kill you too?"
                menu:
                    "YES":
                        c "Nah."
                        jump theEnd
                    "YES":
                        c "Nah."
                        jump theEnd
                    "YES":
                        c "Nah."
                        jump theEnd
                
label secretEnding:
    show char neutral with dissolve
    c "."
    show char interested with dissolve
    c ".."
    show char amazed with dissolve
    c "..."
    c "...."
    c "....."
    c "If you help me get out of here, I will grant you powers."
    menu:
        "How can I help you?":
            show char interested  with dissolve
            c "You alone are not enough, you need help."
            show char neutral with dissolve
            c "In my current state, I cant absorb any chromosomes at all."
            show char interested  with dissolve
            c "But I know,"
            show char interested  with dissolve
            c "even after billions of chromosomes,"
            show char amazed with dissolve
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
            show char neutral with dissolve
            c "At least I dont work 9-5."
            show char interested with dissolve
            c "While living in my mom's basement."
            show char amazed with dissolve
            c "and not subscribed to onlyfans"
            jump theEnd



label badEnding:
    menu:
        "Who are you?":
            show char shocked with dissolve
            c "Just quit, boy. I aint talking w u anymore."

            if not persistent.game_played:
                scene black
                show char dead
                c "Or run the game once again, won't you?"
            else:
                scene black
                show char dead
                c "[pc_name]"
                c "[pc_name] [pc_name] [pc_name]"
                c "Do it all over again correctly, right?"

        
        "Why are you inprisoned here?": 
            show char shocked with dissolve
            c "Just quit, boy. I aint talking w u anymore."

            if not persistent.game_played:
                scene black
                show char dead
                c "Or run the game once again, won't you?"
            else:
                scene black
                show char dead
                c "[pc_name]"
                c "[pc_name] [pc_name] [pc_name]"
                c "Do it all over again correctly, right?"






    # This ends the game.

    return
