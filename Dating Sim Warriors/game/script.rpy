# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

image bg choose = "chooseyourprotagonist.jpg"
image bg coffeeshop = "coffeeshop.jpg"
# Declare characters used by this game.
define s = Character('Sarah', color="#c8ffc8")

#define Sarah
image sarah happy = "sarahhappy.png"


# The game starts here.
label start:
    scene bg choose
    menu:
        "Sorcerer":
            jump sorcerer_start
        "Cyberpunk":
            jump cyberpunk_start
        "Space Marine":
            jump spacemarine_start
label sorcerer_start:
    scene bg coffeeshop
    with fade
    show sarah happy
    with fade
    $ characterclass = 1
    s "Hi I'm Sarah! It's great to meet you."
    s "Oh and fair warning. I'm a bit rusty."
    s "I've been out of the dating scene for a long while"
    s "Oh look at me babbling on and on about myself. So tell me... what do you do?"
    menu:
        "Cast Ray of Frost":
            jump rayoffrost1
        "Cast Magic Missle":
            jump magicmissle1
        "Cast Disrupt Undead":
            jump disruptundead1
        "Cast Bulls Strength":
            jump bullsstrength1
    
label cyberpunk_start:
    $ characterclass = 2
label spacemarine_start:
    $ characterclass = 3
    
    s "Oh Hi! I'm Samantha. It's so nice to meet you."
    show sarah happy
    s "So what do you do?"
    
    return
