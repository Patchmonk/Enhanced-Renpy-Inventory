# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image Forest = "Forest.png"
image Grassland = "Grassland.png"
define e = Character("Eileen")
default gold = 0

# The game starts here.

label start:
    show screen HUD
    show Grassland
    python: 
        inventory = Inventory()
        inventory.add_item("apple", quantity=99)
        inventory.add_item("fish", quantity=5)
        inventory.add_item("apple", quantity=99)
        inventory.add_item("log", quantity=99)
        
    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
