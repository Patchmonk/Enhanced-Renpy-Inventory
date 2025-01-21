# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image inventoryicons = "inventoryicons.png"
image Forest = "Forest.png"
image Grassland = "Grassland.png"
image screenshot_1 = "Screenshot_1.png"
image screenshot_2 = "Screenshot_2.png"
image screenshot_3 = "Screenshot_3.png"
image screenshot_4 = "Screenshot_4.png"
image screenshot_5 = "Screenshot_5.png"
image screenshot_6 = "Screenshot_6.png"
define e = Character("Eileen")
define p = Character("Patchmonk")
default gold = 300



# Inventory initialization
default inventory = Inventory(slot_count=21, unlocked_slots=7)


# The start of the game
label start:
    
    show Grassland
    "Hello friend, welcome to my Enhanced Inventory System tutorial. I'm not sure how you ended up here, but you're in for a treat. If you haven't heard of it, this is the improved version of the simple inventory system."
    "The system relies on two components: a custom notification system and the main inventory system, both nestled in the component folder."
    "So, why is the notification system tangled up with the inventory? Well, I got a bit carried away with my love for fancy sounds and flashy error and success messages. But hey, you can always untangle this mess by editing the code."
    "Don't worry it's super easy you can just return nothing in the function where I call the notification in the main inventory functions. "
    "Now that you're all caught up on the main components and dependencies, it's time to dive into setting this up for your own project. Buckle up, because it's going to be a wild ride!"
    "Just kidding, it's going to be smooth as butter! I made sure it's super easy so anyone can follow along. I mean, as long as you understand basic Ren'py functionality and a little bit of Python syntax."
    
    show screenshot_1
    "Alright, let's get back to business. How do we set up this inventory system in your project? It's as easy as pie, just like its predecessor. Just copy the component folder in your game directory."
    
    "The next step is super simple you have to initialize the variable."
    hide screenshot_1
    show screenshot_2
    "To initialize the variable, you need to create it first and define its parameter before the game starts. It's like setting up your chess pieces before the match begins!"
    "In the screenshot, there are two parameters. The first parameter specifies that the inventory will start with 21 slots. The second parameter designates 7 slots as unlocked from the initial 21 slots, while the remaining slots will be locked."
    "While the rest are locked tighter than treasure chests. You can tweak this setup to match your game style."
    hide screenshot_2

    "Alright, now that you've mastered the inventory setup, let's jump into the fun part the awesome features of this inventory  system!"

    "Just like its predecessor, we'll be rocking the heads-up display with a stylish backpack Icon probably the same one, but who knows? "
    "Designing icons isn't exactly my superpower, but I had to whip up a bunch for this project because the original icon pack author decided to vanish into thin air along with his repository and license. So, I ended up crafting my own icon pack from scratch."
    
    "Now I will activate the HUD screen to display the inventory image button, similar to the previous inventory. However, please be advised that we must close the inventory each time by clicking the cross button; otherwise, we will not be able to continue the tutorial."
    show screen HUD
    "You can open the backpack by clicking the backpack icon to open the inventory system. And don't forget to close it with the cross button in the top right corner, or else The game will stay as like pause mode"
    show screen inventory


    "As you can see, this is an empty inventory. You might be wondering why all the inventory slots have a locked icon. Well, it's obvious because they are locked. This is one of my inventory features. Quite creative, right? Or, you know, who knows. "

    "I've seen it in those big RPG titles where inventory slots are locked, making you grind like crazy. Why not do the same in our small VN? We can always reward the player by unlocking the slots."

    "But hey, it's your call! This is just one of the default features I whipped up. No pressure to use it if you don't want to. We'll save the lock talk for later. First, let's dive into adding the items."

    "An empty inventory is as exciting as watching paint dry. Let's spice things up by adding some items and watch this baby come to life! But first, we need to learn how to add those items."

    show inventoryicons
    "Adding items is a piece of cake! Just head over to the game/components/inventorySystem/images/icons folder and start dropping in your images. Just like those dummy item icons. Easy peasy!"
    "You can edit replace do whatever you want don't forget to remember the dimension of the image and the name is super important as well."
    hide inventoryicons

    "After replacing the default icons with your own item icons, we need to inform the inventory that it's now an item."
    show screenshot_3
    "Since we already have all the images in the icon folder, let's call the add_item function from the inventory system like this screenshot."
    hide screenshot_3
    
    # Add items to the inventory
    $ inventory.add_item("apple", quantity=1)
    $ inventory.add_item("Peach", quantity=1)
    $ inventory.add_item("Strawberry", quantity=1)
    $ inventory.add_item("Pear", quantity=1)
    $ inventory.add_item("Orange", quantity=1)  
    $ inventory.add_item("Pomegranate", quantity=1)


    "We've added some items to the inventory. Let's take a look!"

    show screen inventory

    "Yay, now we are overflowing with items! Our inventory is almost full, and it always gives me a sense of over-accomplishment when something is nearly maxed out. You know that feeling, right?"

    "Some of you might be thinking, 'Yeah, yeah, we've seen it before. You added some items to the inventory. What's the difference?'"

    "My dear friend, unlike the previous inventory which only had basic features, this one has some advanced stuff. Yep, you guessed it right it's stackable items!"

    "Alright, let's add nine more items to each item slot to test this feature."
 
    # Adding 9 More items on each category.
    $ inventory.add_item("apple", quantity=9)
    $ inventory.add_item("Peach", quantity=9)
    $ inventory.add_item("Strawberry", quantity=9)
    $ inventory.add_item("Pear", quantity=9)
    $ inventory.add_item("Orange", quantity=9)  
    $ inventory.add_item("Pomegranate", quantity=9)
    show screen inventory

    "All the item counts have increased isn't it awesome? With stackable items, players can hoard all the items they want."

    "Now you can stack items up to 99 per slot. You can always customize the item limit per slot. The system will automatically take care of redistributing items to existing slots if the items already exist in the inventory."

    "If the items exceed the defined slot limit, they'll be stored in the next available unlocked slot. Pretty cool, right?"

    "If you're wondering what happens if we don't have any slots left and we try to add more items, let me tell you."

    "Well, my friend, I thought about that too! That's why I added a custom notification function to handle such situations. It'll give you an error with a fancy sound and a pop-up message."

    "The fun part about this notification system is that you can customize it to your heart's content. You can use it for other game stuff, customize the style, and the sound too."

    "When a player unlocks something, you can use the notification function to notify them with an accomplishment sound or something."

    "Alright, let's flood our inventory with tons of items to check what our inventory is capable of and enjoy these fancy pop-ups and notifications like those fancy games."

    "Any moment now, the fancy pop-up will show up with a three-second delay. Just hold up, do not click anything, and enjoy."
    
    #Flooding the inventory with tons of items.
    $ inventory.add_item("apple", quantity=99)
    $ inventory.add_item("Peach", quantity=99)
    
    "Ha ha! You saw it, right? Cool, isn't it? I told you at the very beginning that I get carried away with this thing. It's super simple but fancy!"

    "Alright let's check our inventory that error is correct or not? it should Occupy all the available unlock slots."
    
    show screen inventory
    
    "Awesome, all slots are occupied right now. We can't add any more items except for the existing slots up to the slot limit. If you're wondering about the other locked icon slot, we'll come back to this later in the tutorial. Let's complete the basic features first."

    "The simple notification component is modular. I made sure it's modular so you can use it for other game notifications to inform your players about gameplay things."

    "If you don't want such features, I totally get it. It might not be suitable for your game. In that case, you can return nothing. You'll find a section in my code where I'm calling the show_custom_notification function you can edit that. It's super simple!"

    "Alright, now you know how to add items, overflow the inventory, handle errors, and show notifications. We've come so far. So, what's next? Removing items, of course!"

    "How can we remove items from the inventory? If you're wondering how to use the function and how it works, don't worry, we will explore everything."    


    "If you're guessing to remove item you have to call the remove item function you're absolutely correct"
    show screenshot_4
    "This is how you can call the remove item function, In the second parameter you can tell the inventory How many you want to add. Super simple isn't it?"
    
    # Remove items from the inventory
    $ inventory.remove_item("apple", quantity=99)

    hide screenshot_4
    "Our trusty notification system strikes again! It flashed a message and played that oh-so-familiar removal sound, the one that only chimes when items vanish into thin air. As always, feel free to tweak those notifications to match your game’s whims whenever you like."

    "The fun part about the removing function is that it calls the sort function, which shuffles the inventory like a deck of cards."
    
    "So, you don't have to stress about plucking an item from the middle of the inventory crate. Every time you remove something, it will reshuffle itself!"
    
    "I suppose I should also mention that the inventory will play different notifications with sounds based on various scenarios. You can customize all of this to suit your needs."

    "Our Inventory is smart enough to alert you if something goes wrong. For example, we currently have 10 pomegranates in our inventory. If you accidentally try to remove 200 of them, which you don't have, what's going to happen? Let's find out!"
    
    $ inventory.remove_item("Pomegranate", quantity=99)

    
    show screen inventory
    "As you can see, it successfully removed all the items we had, but couldn't remove what we didn't have. That's why we got an error. It gives you a heads-up with a popup message and plays the error sound. Oops, looks like it's time to double-check our inventory!"

    "Now you can add items, remove items, and create your own items. We have all the basic inventory features. I guess we have a complete inventory system now. Hmmm... why do I have this nagging feeling, like last time, that I'm forgetting something?"

    "Hold on a sec... I've just remembered that I promised we'd discuss the locking stuff. Yeah, now I recall you can lock the slots like in those big title games. I was totally inspired by those games inventory!"

    "Alright let's show you how you can unlock all those slot slot in the inventory first. This time also the same like before we have to call our unlock slot function"

    show screenshot_5
    "First, let us demonstrate how to unlock all the slots in the inventory. Like before, we need to call our unlock slot function."
    
    hide screenshot_5

    # Unlock new slots
    $ inventory.unlock_slots(14)

    show screen inventory

    "All our inventory slots are unlocked. That's pretty awesome, right?"

    "By now, you probably know I have a knack for getting carried away. I even created a lock function that can lock all the slots or just a specific number of slots."

    "Honestly, I have no idea what was going through my mind at the time. But imagine if there's a scenario in your game where the character's magic inventory slots get locked due to a curse or something. That's totally possible, right?"

    "Sure, it's not the most common thing, but it doesn't hurt to have it there. It's like one of those items you're hording, just chilling quietly in the background. You don't have to use it if you don't want to."

    "Alright let's lock up few slots to demonstrate this function."
    
    # Lock some slots
    $ inventory.lock_slots(7)

    show screen inventory
    "Kind of depressing, isn't it? After unlocking all the slots, suddenly we lock this row of slots. I'm already feeling really bad, who knows how the player would react to such a thing. Crazy, isn't it? "

    "I can't be the only one getting a twisted sense of satisfaction from this. If you're grinning right now, no judgment here, just saying."












