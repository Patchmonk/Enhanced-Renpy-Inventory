# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image Forest = "Forest.png"
image Grassland = "Grassland.png"
define e = Character("Eileen")
default gold = 300
# Inventory initialization
default inventory = Inventory(slot_count=21, unlocked_slots=7)


# The start of the game
label start:

 
 
  

 
    show screen HUD
    show Grassland
    python: 
       
        
        inventory.add_item("apple", quantity=200)
        inventory.add_item("fish", quantity=5)
        inventory.add_item("apple", quantity=99)
        inventory.add_item("log", quantity=199)
        inventory.add_item("map", quantity=9)  
        inventory.add_item("hurricane ", quantity=1)
     
        
# Initialize the inventory
 

# Increase the slot count by 14 (for example)
        

 
    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"
 

    $ inventory.increase_slot_count(14)  # Slot count is now 35
    "You've increased 14  additional inventory slots!"
    " Awesome more slots!"
    $ inventory.remove_item("apple", quantity=200)
    # This ends the game.
    "Successfully remove 200 items"
    "Successfully remove 200 items"
    "Successfully remove 200 items"
    return
 