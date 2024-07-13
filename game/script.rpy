
default pleased = False
default displeased = False
default liked = False
# default persistent.game_played = False

define lipat = Dissolve(5.0)
define c = Character("???")
define pov = Character("[povname]")

image char amazed = "char_amazed.png"
image char angry = "char_angry.png"
image char neutral = "char_neutral.png"
image char interested = "char_interested.png"
image char shocked = "char_shocked.png"
image char dead = "char_dead.png"
image char eyeless = "char_eyeless.png"


label start:
    jump newGame
    # if not persistent.game_played:
    #     jump newGame
    # else:
        
    #     jump returnGame

    # This ends the game.
    return

