transform zoom_center:
    zoom 2.0
    xpos 0.5
    ypos 1.0
    anchor (0.5, 0.5)

style narrator:
    color "#ffffff"
    size 30
    font "fonts/dealerplate california.otf"

style company:
    color "#e2e2e2"
    size 40
    font "fonts/PlayfairDisplay-Italic-VariableFont_wght.ttf"

default pleased = False
default displeased = False
default liked = False
default persistent.game_played = False


define config.default_music_volume = 1
define config.default_sfx_volume = 0.7

define lipat = Dissolve(10.0)
define c = Character("", what_outlines=[ (.5, "#000000") ], what_color="#ff0080", what_font="fonts/SyneTactile-Regular.ttf")
define pov = Character("[povname]")

image char amazed = "char_amazed.png"
image char angry = "char_angry.png"
image char neutral = "char_neutral.png"
image char interested = "char_interested.png"
image char shocked = "char_shocked.png"
image char dead = "char_dead.png"
image char eyeless = "char_eyeless.png"


image splashScreen1 = "splashScreen1.png"
image splashScreen2 = "splashScreen2.png"
image splashScreen3 = "splashScreen3.png"


label start:
    play music "BGM.mp3"
    if not persistent.game_played:
        jump newGame
    else:
        
        jump returnGame
    return # This ends the game.

