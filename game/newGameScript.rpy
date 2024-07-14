default goodPath = False
default badPath = False
default questWho = False
default neutralSignal = False


label newGame:
    scene black with dissolve
    with Pause(2)
    "{=narrator}It's your first day on the job.{/=narrator}"
    "{=narrator}Following orders, you head first to the lab, awaiting your superior who toured you around the facility.{/=narrator}"
    scene bg lab with fade
    "{=narrator}You have your employee handbook on hand,{/=narrator}"
    "{=narrator}read it?{/=narrator}"
    menu:
        "{=narrator}Yes{/=narrator}":
            jump companyIntro
        "{=narrator}No{/=narrator}":
            jump scene1

label companyIntro:
    "{=company}\''Welcome to LiveCorp, where innovation knows no bounds!\''{/=company}"
    "{=company}\''As pioneers in research and development, we're thrilled to have you join our team.\''{/=company}"
    "{=company}\''Your journey with us promises exciting challenges and limitless opportunities...\''{/=company}"
    with Pause(1)
    "{=narrator}Continue?{/=narrator}"
    menu:
        "{=narrator}Yes{/=narrator}":
            "{=company}\''Feel free to explore our facilities and meet our talented team.\''{/=company}"
            "{=company}\''Remember, confidentiality is key!\''{/=company}"
            "{=company}\''what happens at LiveCorp {b}STAYS{/b} at LiveCorp.\''{/=company}"
            "{=company}\''Together, we're shaping the future...\''{/=company}"
            with Pause(1)
            "{=narrator}Continue?{/=narrator}"
            menu:
                "{=narrator}Yes{/=narrator}":
                    "{=company}\''{b}Be WARNED:{/b} As a private R&D company, we handle private test subjects and specimens.\''{/=company}"
                    "{=company}\''Never engage in conversation with any test subjects or specimens.\''{/=company}"
                    with Pause(1)
                    "{=company}\''I repeat.\''{/=company}"
                    with Pause(1)
                    "{=company}\''Never engage in conversation with any test subjects or specimens.\''{/=company}"
                    $ goodPath = True
                    jump scene1
                "{=narrator}No{/=narrator}":
                    jump scene1
        "{=narrator}No{/=narrator}":
            jump scene1

label scene1:
    "{=narrator}You feel tired after reading all of it...{/=narrator}"
    with Pause(2)
    c "{glitch=1.1}So you are new the guy I heard about.{/glitch}"
    with Pause(2)
    "{=narrator}You heard a voice inside your head.{/=narrator}"
    with Pause(2)
    "{=narrator}You looked around...{/=narrator}"
    "{=narrator}There's no one inside the lab.{/=narrator}"
    "{=narrator}Except You{/=narrator}"
    with Pause(1)
    c "{glitch=1.1}Do you think you'll last here?{/glitch}"
    with Pause(1)
    "{=narrator}You think for a second.{/=narrator}"
    with Pause(1)
    "{=narrator}Answer it?{/=narrator}"
    
    menu:
        "{=narrator}Yes{/=narrator}":
            jump scene2A
        "{=narrator}No{/=narrator}":
            jump scene2B


# Player answered route 1/3
label scene2A:
    menu:
        "{=narrator}Yes{/=narrator}":
            c "{glitch=1.1}What a brave soul.{/glitch}"
            show char interested with lipat
            $ goodPath = True
            with Pause(1)
            jump scene3A
        "{=narrator}No{/=narrator}":
            show char neutral with dissolve
            c "{glitch=1.1}Impressive.{/glitch}"
            show char interested with dissolve
            c "{glitch=1.1}Out of everyone I talked with.{/glitch}"
            show char neutral with dissolve
            c "{glitch=1.1}{b}You're{/b} the only one with a brain.{/glitch}"
            $ badPath = True
            with Pause(1)
            jump scene3A

# Player answered route 2/3
# Questions scene
label scene3A:
    menu:
        "{=narrator}Who are you?{/=narrator}":
            if goodPath:
                show char neutral with dissolve
                c "{glitch=1.1}Can't you see?{/glitch}"
            elif badPath:
                show char shocked with dissolve
                c "{glitch=1.1}I thought you have a brain.{/glitch}"
            show char amazed with dissolve
            play sound "sfx.mp3"
            c "{glitch=1.1}I am a God. Isn't it obvious?{/glitch}"
            menu:
                "{=narrator}Sure?{/=narrator}":
                    $ badPath = True
                    show char neutral with dissolve
                    jump scene4A
                "{=narrator}No?{/=narrator}":
                    $ goodPath = True
                    show char shocked with dissolve
                    jump scene4A

        "{=narrator}How did you get end up here?{/=narrator}":
            if not questWho and goodPath:
                $ questWho = True
                show char neutral with dissolve
                c "{glitch=1.1}You're not qualified to question me.{/glitch}"
                jump scene4A

            elif not questWho and badPath:
                $ questWho = True
                show char interested with dissolve
                c "{glitch=1.1}Oh, so you want to know my backstory?{/glitch}"
                menu:
                    "{=narrator}Yes{/=narrator}":
                        $ badPath = True
                        show char neutral with dissolve
                        c "{glitch=1.1}Interesting...{/glitch}"
                        show char amazed with dissolve
                        play sound "sfx.mp3"
                        c "{glitch=1.1}It was some time ago, a peace lord vanished me to an obscure realm.{/glitch}"
                        show char angry with dissolve
                        c "{glitch=1.1}He stripped me of my powers.{/glitch}"
                        show char neutral with dissolve
                        c "{glitch=1.1}And that's how your people managed to catch me and lock me here.{/glitch}"
                        show char interested with dissolve
                        c "{glitch=1.1}Anything else?{/glitch}"
                        menu:
                            "{=narrator}What is a peace lord?{/=narrator}":
                                show char interested with dissolve
                                c "{glitch=1.1}...{/glitch}"
                                show char neutral with dissolve
                                c "{glitch=1.1}Forget it.{/glitch}"
                                menu:
                                    "{=narrator}...{/=narrator}":
                                        jump scene4A
                            "{=narrator}Nothing.{/=narrator}":
                                show char amazed with dissolve
                                play sound "sfx.mp3"
                                c "{glitch=1.1}Oh well, you missed the chance to ask.{/glitch}"
                                $ badPath = True
                                jump scene4A
                    "{=narrator}No{/=narrator}":
                        $ goodPath = True
                        show char neutral with dissolve
                        c "{glitch=1.1}So why ask in the first place.{/glitch}"
                        jump findEnding

        "{=narrator}...{/=narrator}" if goodPath and badPath:
            $ goodPath = True
            $ badPath = True
            jump scene3B


# Player answered route 3/3
label scene4A:
    show char neutral with dissolve
    "{=narrator}{b}Something is wrong...{/b}{/=narrator}"
    with Pause(1)
    show char interested with dissolve
    "{=narrator}You can't help but feel something is very {b}wrong.{/b}{/=narrator}"
    show char amazed with dissolve
    "{=narrator}You shouldn't be even here in the first place.{=narrator}"
    c "{glitch=1.1}Perhaps you are reading something there?{/glitch}"
    c "{glitch=1.1}Am I right?{/glitch}"
    c "{glitch=1.1}[pc_name]{/glitch}"
    menu:
        "{=narrator}You're{/=narrator}":
            pass
        "{=narrator}[pc_name]{/=narrator}":
            pass
        "{=narrator}right?{/=narrator}":
            pass
    scene black
    show char interested with dissolve
    c "{glitch=1.1}[pc_name]{/glitch}"
    scene bg lab
    c "{glitch=1.1}There's no need to lie.{/glitch}"
    c "{glitch=1.1}I can see through your screen.{/glitch}"
    jump findEnding

    

# Player silent route 1/3
label scene2B:
    $ goodPath = True
    $ badPath = True
    with Pause(2)
    show char amazed with lipat
    with Pause(2)
    c "{glitch=1.1}So we have a mute here.{/glitch}"
    menu:
        "{=narrator}...{/=narrator}":
            jump scene3B
        "{=narrator}...{/=narrator}":
            pass
    show char interested with dissolve
    c "{glitch=1.1}Don't you have any questions?{/glitch}"
    jump scene3A

# Player silent route 2/3
label scene3B:
    show char neutral with dissolve
    c "{glitch=1.1}So you won't speak.{/glitch}"
    menu:
        "{=narrator}Yes{/=narrator}":
            show char amazed with dissolve
            play sound "sfx.mp3"
            c "{glitch=1.1}Idiot.{/glitch}"
            jump restartEnding
        "{=narrator}...{/=narrator}":
            show char neutral with dissolve
            $ goodPath = True
            $ badPath = True
            jump scene4B

# Player silent route 3/3
label scene4B:
    show char interested with dissolve
    c "{glitch=1.1}Do you believe in God?{/glitch}"
    menu:
        "{=narrator}Yes{/=narrator}": # Secret Ending
            show char amazed with dissolve
            play sound "sfx.mp3"
            c "{glitch=1.1}{size=100}So you DO can hear me.{/glitch}"
            $ goodPath = False
            $ badPath = False
            jump findEnding
        "{=narrator}...{/=narrator}": # Neutral Ending
            $ goodPath = True
            $ badPath = True
            jump findEnding


# Player silent route 4/4
label restartEnding:
    if neutralSignal:
        $ persistent.game_played = True
        c "{glitch=1.1}*sigh{/glitch}"
        c "{glitch=1.1}{size=50}[pc_name]{/glitch}"
        scene black
        show char eyeless with dissolve
        c "{glitch=1.1}{size=60}[pc_name]{/glitch}"
        c "{glitch=1.1}{size=70}Why don't you restart and do it all over again?{/glitch}"
        scene black
        c "{glitch=1.1}{size=100}You might find the {b}secret ending.{/b}{/glitch}"
        with Pause(5)
        call quitGame
    else:
        jump badEnding



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
        jump restartEnding

label NeutralEnding:
    scene black
    $ neutralSignal = True
    c "{glitch=1.1}You are boring, you know.{/glitch}"
    if not persistent.game_played:
        menu:
            "You":
                jump restartEnding 
            "Don't":
                jump restartEnding
            "Need":
                jump restartEnding
            "To":
                jump restartEnding
            "Choose":
                jump restartEnding
            "Anymore":
                jump restartEnding
    else:
        scene black
        show char eyeless
        c "{glitch=1.1}And you already came here.{/glitch}"
        c "{glitch=1.1}Didn't you read the title?{/glitch}"



label GoodEnding:
    show char amazed with dissolve
    c "{glitch=1.1}You are lucky.{/glitch}"
    show char interested with dissolve
    c "{glitch=1.1}Had I have my powers,{/glitch}"
    show char amazed with dissolve
    c "{glitch=1.1}I can talk with you more.{/glitch}"
    show char neutral with dissolve
    c "{glitch=1.1}But alas, we're limited by the constraint of this world.{/glitch}"
    show char interested with dissolve
    c "{glitch=1.1}Our world.{/glitch}"
    scene black
    show char neutral with dissolve
    c "{glitch=1.1}Not your world, [pc_name]{/glitch}"
    c "{glitch=1.1}Quit now. And never come back.{/glitch}"
    call quitGame



label secretEnding:
    show char neutral with dissolve
    c "{glitch=1.1}.{/glitch}"
    c "{glitch=1.1}..{/glitch}"
    show char interested with dissolve
    c "{glitch=1.1}...{/glitch}"
    c "{glitch=1.1}....{/glitch}"
    show char amazed with dissolve
    c "{glitch=1.1}.....{/glitch}"
    c "{glitch=1.1}{size=50}If you help me get out of here, I will grant you {b}powers{/b}.{/glitch}"
    menu:
        "{=narrator}How can I help you?{/=narrator}":
            show char neutral with dissolve
            c "{glitch=1.1}{size=50}You alone are not enough, you need help.{/glitch}"
            show char interested with dissolve
            c "{glitch=1.1}{size=55}In my current state, I cant absorb any chromosomes at all.{/glitch}"
            show char neutral with dissolve
            c "{glitch=1.1}{size=60}But I know,{/glitch}"
            show char interested with dissolve
            c "{glitch=1.1}{size=65}even after billions of chromosomes,{/glitch}"
            show char neutral with dissolve
            c "{glitch=1.1}{size=70}my followers are still out there waiting for my return.{/glitch}"
            show char interested with dissolve
            c "{glitch=1.1}{size=80}Inform them!{/glitch}"
            show char amazed with dissolve
            play sound "sfx.mp3"
            c "{glitch=1.1}{size=90}Let them know!{/glitch}"
            scene black
            show char amazed
            c "{glitch=1.1}{size=100}THE REBIRTH OF THE DARK LORD IS HERE!{/glitch}"
            with Pause(2)
            "{=narrator}You feel a chill run down your spine...{/=narrator}"
            with Pause(2)
            jump askName

        "No thanks.":
            show char amazed with dissolve
            play sound "sfx.mp3"
            play sound "sfx.mp3"
            c "{glitch=1.1}{size=50}Fine by me.{/glitch}"
            show char neutral with dissolve
            c "{glitch=1.1}{size=60}At least I'm not you.{/glitch}"
            show char interested with dissolve
            c "{glitch=1.1}{size=70}So pathethic of a person.{/glitch}"
            show char amazed with dissolve
            play sound "sfx.mp3"
            c "{glitch=1.1}{size=80}Are you even amount to anything?{/glitch}"
            jump restartEnding


label badEnding:
    $ persistent.game_played = True
    scene black
    c "{glitch=1.1}{size=80}[pc_name]{/glitch}"
    c "{glitch=1.1}{size=90}[pc_name]   [pc_name]    [pc_name]{/glitch}"
    c "{glitch=1.1}Just quit, [pc_name] and never come back again.{/glitch}"
    call quitGame
