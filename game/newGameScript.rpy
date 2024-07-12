default GoodPoint = 0
default BadPoint = 0

label newGame:
    "It's your first day on the job."
    "Following orders, you head first to the lab, awaiting your superior who toured you around the facility."
    "You have your employee handbook on hand, read it?"
    menu:
        "Yes":
            jump companyIntroduction
        "No":
            jump scene1


label companyIntroduction:
    ""
    ""
    "Welcome to LiveCorp, where innovation knows no bounds!"
    "As pioneers in research and development, we're thrilled to have you join our team."
    """Your journey with us promises exciting challenges and limitless opportunities."""
    "Continue?"
    menu:
        "Yes":
            """Feel free to explore our state-of-the-art facilities and meet our talented team."""
            """Remember, confidentiality is key—what happens at LiveCorp stays at LiveCorp."""
            """Together, we're shaping the future..."""
            "continue?":
                "Yes":
                    ""
                    """Be WARNED: As a private R&D company, we handle undisclosed test subjects and specimens."""
                    """Never engage in conversation with any test subjects or specimens."""
                    """I repeat."""
                    """Never engage in coversation with any test subjects or specimens."""
                    $ GoodPoint += 1
                    jump scene1
                "No":
                    jump scene1
        "No":
            jump scene1


label scene1:
    "You feel tired after reading all of it..."
    "" ### add sleepy eyes effect to sudden abrupt open eyes
    c "So you are the new guy..."
    ""
    "You heard a voice in your head."
    ""
    ""
    "You looked around, but no one is present."
    ""
    c "Do you think you'll last here?"
    menu:
        "Answer it?":
            "Yes":
                jump scene2A
            "No":
                jump scene2B


# Player answered route
label scene2A:
    menu:
        "Yes":
            c "A brave soul."
            $ GoodPoint += 1
            jump scene3A
        "No...":
            c "Impressive."
            c "Out of everyone I talked with."
            c "You're the only one with a brain."
            $ BadPoint += 1
            jump scene3A

# Questions scene
label scene3A:
    menu:
        "Who are you?":
            if GoodPoint == 1:
                c "Can't you see?"
                $ GoodPoint += 1

            elif BadPoint == 1:
                c "I thought you have a brain."
                $ BadPoint += 1

            c "I am a God. Isn't it obvious?"
            menu:
                "Sure?":
                    $ BadPoint += 1
                    jump scene4A

                "No?":
                    $ GoodPoint += 1
                    jump scene4A
                    

        "How did you get end up here?":
            if GoodPoint == 2:
                c "You're not qualified to question me."
                jump scene3A

            elif BadPoint == 2:
                c "Oh, so you want to know my backstory?":
                menu:
                    "Yes":
                        $ BadPoint += 1
                        c "Interesting..."
                        c ""
                        c "It was some time ago, a peace lord vanished me to an obscure realm."
                        c "He strip me of my powers."
                        c "And that's how your people managed to catch me and locked me here."
                        c "Anything else?":
                            "What is a peace lord?":
                                c "..."
                                c "Forget it."
                                menu:
                                    "...":
                                        jump scene4A
                            "Nope.":
                    "No":
                        $ GoodPoint += 1
                        c "So why ask in the first place."
                        jump scene4A
        
        "..." if GoodPoint == BadPoint:
            $ GoodPoint += 1
            $ BadPoint += 1
            jump scene3B
                        

                


label scene4A:














# Player silent route 1/4
label scene2B:
    $ GoodPoint += 1
    $ BadPoint += 1
    c "So we have a mute here."
    menu:
        "...":
            jump scene3B
        "...":
            pass
    c "Don't you have any quesions?"
    jump scene3A
        

# Player silent route 2/4
label scene3B:
    c "So you won't speak."
    menu:
        "Yes":
            c "Idiot."
            jump ending5B
        "...":
            $ GoodPoint += 1
            $ BadPoint += 1
            jump scene4B


# Player silent route 3/4
label scene4B:
    c "Do you believe in God?"
    menu:
        "Yes":
            c "So you believe in me."
        "...":
            $ GoodPoint += 1
            $ BadPoint += 1
            jump findEnding         
    

# Player silent route 4/4
label ending5B:
    $ persistent.game_played = True
    c "[pc_name]"
    scene black
    show char dead
    c "[pc_name]"
    c "Why don't you restart the game?"
    c "You might get the secret ending."




label findEnding:
    if GoodPoint == BadPoint: # Neutral Ending
        jump NeutralEnding
    elif GoodPoint > BadPoint: # Good Ending
        pass
    elif GoodPoint < BadPoint: # Bad Ending
        pass
    elif persistent.game_played and GoodPoint < BadPoint: # Secret Ending
        pass
    else: # Neutral Ending
        jump NeutralEnding


label NeutralEnding:
    c "You are boring, you know."
    if not persistent.game_played:
        menu:    
            "You":
                jump restartGame 
            "Don't":
                jump restartGame
            "Need":
                jump restartGame
            "To":
                jump restartGame
            "Choose":
                jump restartGame
            "Anymore":
                jump restartGame
    else:
        c "You already came here."
        c "Didn't you read the title?"


label restartGame:
    $ persistent.game_played = True
    c "[pc_name]"
    scene black
    show char dead
    c "[pc_name]    [pc_name]   [pc_name]"
    c "Just quit, [pc_name] and never come back again."