# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image Forest = "Forest.png"
image Grassland = "Grassland.png"
define e = Character("Eileen")
default gold = 300
# Inventory initialization
default inventory = Inventory(slot_count=21, unlocked_slots=7)

# The game starts here.
 
 
label start:
    show screen HUD
    show Grassland
    python: 
        inventory.unlock_slots(5)
        
        inventory.add_item("apple", quantity=200)
        inventory.add_item("fish", quantity=5)
        inventory.add_item("apple", quantity=99)
        inventory.add_item("log", quantity=199)
        inventory.add_item("map", quantity=9)  
        inventory.add_item("hurricane ", quantity=1)
     
        

 
    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"
     
 
    "You've unlocked 7 additional inventory slots!"
    " Awesome more slots!"

    # This ends the game.

    return
