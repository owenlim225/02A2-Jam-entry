default goodPath = False
default badPath = False
default questWho = False

label newGame:
    "It's your first day on the job."
    "Following orders, you head first to the lab, awaiting your superior who toured you around the facility."
    scene bg lab with fade
    "You have your employee handbook on hand,"
    "read it?"
    menu:
        "Yes":
            jump companyIntro
        "No":
            jump scene1

label companyIntro:
    "Welcome to LiveCorp, where innovation knows no bounds!"
    "As pioneers in research and development, we're thrilled to have you join our team."
    "Your journey with us promises exciting challenges and limitless opportunities."
    "Continue?"
    menu:
        "Yes":
            "Feel free to explore our facilities and meet our talented team."
            "Remember, confidentiality is key!"
            "what happens at LiveCorp STAYS at LiveCorp."
            "Together, we're shaping the future..."
            "Continue?"
            menu:
                "Yes":
                    "Be WARNED: As a private R&D company, we handle undisclosed test subjects and specimens."
                    "Never engage in conversation with any test subjects or specimens."
                    "I repeat."
                    "Never engage in conversation with any test subjects or specimens."
                    $ goodPath = True
                    jump scene1
                "No":
                    jump scene1
        "No":
            jump scene1

label scene1:
    "You feel tired after reading all of it..."
    ""
    scene guide
    c "So you are new the guy I heard about."
    ""
    "You heard a voice inside your head."
    ""
    ""
    "You looked around..."
    "There's no one inside the lab."
    "Except You..."
    ""
    ""
    c "Do you think you'll last here?"
    ""
    "You think for a second."
    "Answer it?"
    menu:
        "Yes":
            jump scene2A
        "No":
            jump scene2B


# Player answered route 1/3
label scene2A:
    show char interested with lipat
    menu:
        "Yes":
            show char amazed with dissolve
            c "What a brave soul."
            $ goodPath = True
            jump scene3A
        "No":
            show char neutral with dissolve
            c "Impressive."
            show char interested with dissolve
            c "Out of everyone I talked with."
            show char neutral with dissolve
            c "You're the only one with a brain."
            $ badPath = True
            jump scene3A

# Player answered route 2/3
# Questions scene
label scene3A:
    menu:
        "Who are you?":
            if goodPath:
                show char neutral with dissolve
                c "Can't you see?"
            elif badPath:
                show char shocked with dissolve
                c "I thought you have a brain."
            show char amazed with dissolve
            c "I am a God. Isn't it obvious?"
            menu:
                "Sure?":
                    $ badPath = True
                    show char neutral with dissolve
                    jump scene4A
                "No?":
                    $ goodPath = True
                    show char shocked with dissolve
                    jump scene4A

        "How did you get end up here?":
            if not questWho and goodPath:
                $ questWho = True
                show char neutral with dissolve
                c "You're not qualified to question me."
                jump scene4A

            elif not questWho and badPath:
                $ questWho = True
                show char interested with dissolve
                c "Oh, so you want to know my backstory?"
                menu:
                    "Yes":
                        $ badPath = True
                        show char neutral with dissolve
                        c "Interesting..."
                        show char amazed with dissolve
                        c "It was some time ago, a peace lord vanished me to an obscure realm."
                        show char angry with dissolve
                        c "He stripped me of my powers."
                        show char neutral with dissolve
                        c "And that's how your people managed to catch me and lock me here."
                        show char interested with dissolve
                        c "Anything else?"
                        menu:
                            "What is a peace lord?":
                                show char interested with dissolve
                                c "..."
                                show char neutral with dissolve
                                c "Forget it."
                                menu:
                                    "...":
                                        jump scene4A
                            "Nothing.":
                                show char amazed with dissolve
                                c "Oh well, you missed the chance to ask."
                                $ badPath = True
                                jump scene4A
                    "No":
                        $ goodPath = True
                        show char neutral with dissolve
                        c "So why ask in the first place."
                        jump findEnding

        "..." if goodPath and badPath:
            $ goodPath = True
            $ badPath = True
            jump scene3B


# Player answered route 3/3
label scene4A:
    show char neutral with dissolve
    "Something is wrong..."
    show char interested with dissolve
    "You can't help but feel something is very wrong."
    show char amazed with dissolve
    "You shouldn't be even here in the first place."
    c "Perhaps you are reading something there?"
    c "Am I right?"
    menu:
        "...":
            pass
        "...":
            pass
        "...":
            pass
    scene black
    show char interested with dissolve
    c "[pc_name]"
    scene bg lab
    c "There's no need to lie."
    c "I can see through you."
    jump findEnding

    

# Player silent route 1/3
label scene2B:
    $ goodPath = True
    $ badPath = True
    show char amazed with dissolve
    c "So we have a mute here."
    menu:
        "...":
            jump scene3B
        "...":
            pass
    show char interested with dissolve
    c "Don't you have any questions?"
    jump scene3A

# Player silent route 2/3
label scene3B:
    show char neutral with dissolve
    c "So you won't speak."
    menu:
        "Yes":
            show char amazed with dissolve
            c "Idiot."
            jump restartEnding
        "...":
            show char neutral with dissolve
            $ goodPath = True
            $ badPath = True
            jump scene4B

# Player silent route 3/3
label scene4B:
    show char interested with dissolve
    c "Do you believe in God?"
    menu:
        "Yes": # Secret Ending
            show char amazed with dissolve
            c "So you believe in me."
            $ goodPath = False
            $ badPath = False
            jump findEnding
        "...": # Neutral Ending
            $ goodPath = True
            $ badPath = True
            jump findEnding


# Player silent route 4/4
label restartEnding:
    $ persistent.game_played = True
    c "*sigh"
    c "[pc_name]"
    scene black
    show char dead
    c "[pc_name]"
    c "Why don't you restart the game?"
    show char eyeless
    c "You might get the secret ending."



# Find the best ending for player based on points
label findEnding:
    if goodPath and badPath: # Neutral Ending
        jump NeutralEnding
    elif goodPath and not badPath: # Good Ending
        jump GoodEnding
    elif not goodPath and badPath: # Bad Ending
        jump badEnding
    elif persistent.game_played and not goodPath and not badPath: # Secret Ending
        jump secretEnding
    else: # Neutral Ending
        jump NeutralEnding

label NeutralEnding:
    scene black
    show char dead 
    c "You are boring, you know."
    if not persistent.game_played:
        menu:
            "You":
                jump badEnding 
            "Don't":
                jump badEnding
            "Need":
                jump badEnding
            "To":
                jump badEnding
            "Choose":
                jump badEnding
            "Anymore":
                jump badEnding
    else:
        scene black
        show char eyeless
        c "And you already came here."
        c "Didn't you read the title?"



label GoodEnding:
    show char amazed with dissolve
    c "You are lucky."
    show char interested with dissolve
    c "Had I have my powers,"
    show char amazed with dissolve
    c "I can talk with you more."
    show char neutral with dissolve
    c "But alas, we're limited by the constraint of this world."
    show char interested with dissolve
    c "Our world."
    scene black
    show char neutral with dissolve
    c "Not your world, [pc_name]"
    c "Quit now. And never come back."



label secretEnding:
    show char neutral with dissolve
    c "."
    c ".."
    show char interested with dissolve
    c "..."
    c "...."
    show char amazed with dissolve
    c "....."
    c "If you help me get out of here, I will grant you powers."
    menu:
        "How can I help you?":
            show char interested with dissolve
            c "You alone are not enough, you need help."
            show char neutral with dissolve
            c "In my current state, I cant absorb any chromosomes at all."
            show char interested with dissolve
            c "But I know,"
            show char interested with dissolve
            c "even after billions of chromosomes,"
            show char amazed with dissolve
            c "my followers are still out there waiting for my return."
            c "Inform them! "
            c "Let them know!"
            show char amazed with dissolve
            c "THE REBIRTH OF THE DARK LORD IS HERE!"
            "You feel a chill run down your spine..."
            jump askName

        "No thanks.":
            show char interested with dissolve
            c "Fine by me."
            show char neutral with dissolve
            c "At least I'm not you."
            show char interested with dissolve
            c "So pathethic of a person."
            show char amazed with dissolve
            c "Are you even amount to anything?"
            jump restartEnding


label badEnding:
    $ persistent.game_played = True
    c "[pc_name]"
    scene black
    show char dead
    c "[pc_name] [pc_name] [pc_name]"
    c "Just quit, [pc_name] and never come back again."
