# The script of the game goes in this file.

# ⚙️ Declare characters used by this game.
# The color argument colorizes the name of the character.

# 🖼️ Define image assets used in the tutorial
# These lines give short, easy-to-remember names to image files.
image inventoryicons = "inventoryicons.png"
image Forest = "Forest.png"
image Grassland = "Grassland.png"
image Grassland_sunset = "Grassland_sunset.png"
image Apple_road = "Apple_road.png"
image Orange_road = "Orange_road.png"
# 🖼️ Screenshots for visual aids during the tutorial
image screenshot_1 = "Screenshot_1.png"
image screenshot_2 = "Screenshot_2.png"
image screenshot_3 = "Screenshot_3.png"
image screenshot_4 = "Screenshot_4.png"
image screenshot_5 = "Screenshot_5.png"
image screenshot_6 = "Screenshot_6.png"
image screenshot_7 = "Screenshot_7.png"
image screenshot_8 = "Screenshot_8.png"

# 👤 Define characters for dialogue
define e = Character("Eileen") # Just an example character, you can change this!
define p = Character("Patchmonk") # Your friendly tutorial guide!

# 💾 Define default persistent variables
# 'persistent' means these values save even when the player quits.
default gold = 300 # Example variable, not really used by the inventory itself.




# 🎬 The start of the game and the tutorial
label start:
    show Grassland
 
    p "Ahoy, matey! Welcome to the enchanted forest of Ren'py. You've found the ultimate inventory system tutorial. Brace yourself for a wild ride filled with fruity adventures and epic loot!"
    p "This system is the Swiss Army knife of inventory systems. It comes equipped with two main component: a notification system and the main inventory system."
    p "The notification system was supposed to be a future project, but I got a little overexcited and built it anyway. It’s still a work in progress, but a fancier version is coming soon."
    p "If all the razzle-dazzle isn't your thing, just return nothing in the main Inventory functions where the notification function is called. Simple as pie, easy as a sigh!"    
    p "Now that you're all caught up on the main components, it's time to dive into setting this up for your own project. Buckle up, because it's going to be a wild ride!"
    p "Just kidding, it's going to be smooth as butter! I made sure it's super easy so anyone can follow along. I mean, as long as you understand basic Ren'py functionality and a little bit of Python syntax."

    show screenshot_1

    p "Alright, let's get back to business. How do we set up this inventory system in your project? It's as easy as pie."
    p "Simply grab that component folder and toss it into your game folder, just like the screenshot is flaunting right now."
    
    hide screenshot_1

 
    p "Alright, now that you've mastered the inventory setup, let's jump into the fun part the awesome features of this inventory system!"
    p "Just like its predecessor, we'll be rocking the heads-up display (HUD) with a stylish backpack icon. Probably the same one, but who knows? Designing icons isn't exactly my superpower"
    p "Now I'll activate the HUD screen to display the inventory image button, similar to the previous inventory. "
    p "However, please be advised that we must close the inventory each time by clicking the cross button in the top-right corner. Otherwise, the game will freeze like a startled turtle."
    
    # ⚙️ Show the Heads-Up Display (HUD) screen. This usually stays on screen.
    show screen HUD
    p "You can open the backpack by clicking the backpack icon to open the inventory system. Don't forget to close it with the cross button, or else the game will stay paused forever. No pressure!"
    # ⚙️ Show the main inventory screen. This pops up when needed.
    
    show screen inventory
    p "As you can see, this inventory is currently empty. You may notice that many of the inventory slots display a locked icon. That's because they are indeed locked. This is one of the features of my inventory system. Quite creative, isn't it? Or perhaps not."
    p "You've probably seen it before in RPG games where locked inventory slots make you grind like a maniac. A handy feature, right? It spices up the game! Why not add the same feature to our game? We can always reward players by unlocking new slots."
    p "But hey, it's your call! This is just one of the default features I whipped up. No pressure to use it if you don't want to. We'll save the lock talk for later. First, let's dive into adding the items."
    p "An empty inventory is as exciting as watching paint dry. Let's spice things up by adding some items and watch this baby come to life! But first, we need to learn how to add those items."
    
    show inventoryicons
    p "Adding items is a piece of cake! Just head over to the `game/components/inventorySystem/images/icons` folder and start dropping in your images. Just like those dummy item icons. Easy peasy!"
    p "You can edit, replace, or do whatever you want. Just don't forget the dimensions of the images, and the name is super important. Otherwise, the system won't recognize it."
    
    hide inventoryicons
    p "After replacing the default icons with your own item icons, we need to inform the inventory that it's now an item."
    
    show screenshot_3
    p "Since we already have all the images in the icon folder, let's call the `add_item` function from the inventory system like this screenshot."
    hide screenshot_3
    
    # ➕ Adding items to the inventory.
    # 👇 This Python block adds several items at once. Nice and tidy!
    # 💡 You can also add one item like this: $ inventory.add_item("Apple", quantity=1)
    python:
        inventory.add_item("Apple", quantity=1)
        inventory.add_item("Peach", quantity=1)
        inventory.add_item("Strawberry", quantity=1)
        inventory.add_item("Pear", quantity=1)
        inventory.add_item("Orange", quantity=1)
        inventory.add_item("Pomegranate", quantity=1)
    p "We've added some items to the inventory. Let's take a look!"
    # ⚙️ Show the inventory screen again to see the new items.
    
    show screen inventory
    p "Yay, now we are overflowing with items! Our inventory is almost full, and it always gives me a sense of over-accomplishment when something is nearly maxed out. You know that feeling, right?"
    p "Some of you might be thinking, 'Yeah, yeah, we've seen it before. You added some items to the inventory. What's the difference?'"
    p "My dear friend, unlike the previous inventory which only had basic features, this one has some advanced stuff. Yep, you guessed it right it's stackable items!"
    p "Alright, let's add nine more items to each item slot to test this feature."
   
    # ➕ Adding *more* items to the inventory to test stacking.
    # 👇 Again, using a Python block is good for adding multiple things.
    # 💡 Single item add example: $ inventory.add_item("Apple", quantity=9)
    python:
        inventory.add_item("Apple", quantity=9)
        inventory.add_item("Peach", quantity=9)
        inventory.add_item("Strawberry", quantity=9)
        inventory.add_item("Pear", quantity=9)
        inventory.add_item("Orange", quantity=9)
        inventory.add_item("Pomegranate", quantity=9)
    # ⚙️ Show the inventory screen to see the stacked items.
    
    show screen inventory
    p "All the item counts have increased isn't it awesome? With stackable items, players can hoard all the items they want."
    p "Now you can stack items up to 99 per slot. You can always customize the item limit per slot. The system will automatically take care of redistributing items to existing slots if the items already exist in the inventory."
    p "If the items exceed the defined slot limit, they'll be stored in the next available unlocked slot. Pretty cool, right?"
    p "If you're wondering what happens if we don't have any slots left and we try to add more items, let me tell you."
    p "My friend, I thought about that too! That's why I added a custom notification function to handle such situations. It'll give you an error with a fancy sound and a pop-up message."
    p "The fun part about this notification system is that you can customize it to your heart's content. You can use it for other game stuff, customize the style, and the sound too."
    p "When a player unlocks something, you can use the notification function to notify them with an accomplishment sound or something."
    p "Alright, let's flood our inventory with tons of items to check what our inventory is capable of and enjoy these fancy pop-ups and notifications like those fancy games."
    p "Now, if you hit the keyboard or click your mouse, a fancy popup notification will appear on your screen. Gaze at it for 3 seconds before proceeding to the next dialogue."
    
    # ⚠️ Trying to add way too many items to trigger the 'inventory full' notification.
    $ inventory.add_item("Apple", quantity=99)
    $ inventory.add_item("Peach", quantity=99) 
    
    p "Ha ha! You saw it, right? Cool, isn't it? I told you at the very beginning that I get carried away with this thing. It's super simple but fancy!"
    p "Alright, let's check our inventory that error is correct or not. It should occupy all the available unlocked slots."
    # ⚙️ Show the inventory screen to confirm it's full.
    
    show screen inventory
    p "Awesome, all slots are occupied right now. We can't add any more items except for the existing slots up to the slot limit. "
    p "If you're wondering about the other locked icon slot, we'll come back to this later in the tutorial. Let's complete the basic features first."
    p "The simple notification component is modular. I made sure it's modular so you can use it for other game notifications to inform your players about gameplay things."
    p "If you don't want such features, I totally get it. It might not be suitable for your game. In that case, you can return nothing. "
    p "In the main 'inventory.rpy' file code where the 'pm_notify()' functions is called, simply remove or comment out the function to ensure it does not execute or trigger any actions."
  
    p "Alright, now you know how to add items, overflow the inventory, handle errors, and show notifications. We've come so far. So, what's next? Removing items, of course!"
    p "How can we remove items from the inventory? If you're wondering, 'Is this function like adding items?"
    p "Yep, you guessed it! You're absolutely right it’s very similar to the add item function."

    # 🖼️ Showing screenshot number 4
    show screenshot_4
    p "This is how you can call the `remove_item` function. In the second parameter, you can tell the inventory how many you want to remove. Super simple, isn't it?"
    # ➖ Removing 99 Apples from the inventory.
    $ inventory.remove_item("Apple", quantity=99)
    
    hide screenshot_4
    p "Our trusty notification system strikes again! It flashed a message and played that oh-so-familiar removal sound the one that only chimes when items vanish into thin air."
    p "As always, feel free to tweak those notifications to match your game's whims whenever you like."
    p "The fun part about the removing function is that it calls the sort function, which shuffles the inventory like a deck of cards."
    p "So, you don't have to stress about plucking an item from the middle of the inventory crate. Every time you remove something, it will reshuffle itself!"
    p "I suppose I should also mention that the inventory will play different notifications with sounds based on various scenarios. You can customize all of this to suit your needs."
    p "Our inventory is smart enough to alert you if something goes wrong. For example, we currently have 10 pomegranates in our inventory. "
    p "Currently, there are 10 Pomegranates in the inventory. If you mistakenly attempt to remove 200, which exceeds the available quantity, what will happen? Let us find out!"

    # ⚠️ Trying to remove *more* items than we actually have to trigger an error notification.
    $ inventory.remove_item("Pomegranate", quantity=200)

    # ⚙️ Show the inventory screen to see the result of removing items.
    show screen inventory

    p "As you can see, it successfully removed all the items we had, but couldn't remove what we didn't have. That's why we got an error. It gives you a heads-up with a popup message and plays the error sound."
    p "Now you can add items, remove items, and create your own items. We have all the basic inventory features. I guess we have a complete inventory system now."
    p "Hmm… why do I have this nagging feeling, like last time, that I'm forgetting something?"
    p "Hold on a sec… I've just remembered that I promised we'd discuss the locking stuff. Yeah, now I recall you can lock the slots like in those big title games. I was totally inspired by those games' inventories!"
    p "Alright, let's show you how you can unlock all those slots in the inventory first. This time, it's the same as before we have to call our `unlock_slots` function."

    # 🖼️ Showing screenshot number 5
    show screenshot_5
    
    p "First, let's demonstrate how to unlock all the slots in the inventory. Like before, we need to call our `unlock_slots` function."
    # 🖼️ Hiding screenshot number 5
    
    hide screenshot_5
    # 🔓 Unlock 14 more slots (we started with 7, 7 + 14 = 21 total initial slots).
    $ inventory.unlock_slots(14)
    # ⚙️ Show inventory to see the newly unlocked slots.
    
    show screen inventory
    p "All our inventory slots are unlocked. That's pretty awesome, right?"
    p "By now, you probably know I have a knack for getting carried away. I even created a lock function that can lock all the slots or just a specific number of slots."
    p "Honestly, I have no idea what was going through my mind at the time. But imagine if there's a scenario in your game where the character's magic inventory slots get locked due to a curse or something. That's totally possible, right?"
    p "Sure, it's not the most common thing, but it doesn't hurt to have it there. It's like one of those items you're hoarding, just chilling quietly in the background. You don't have to use it if you don't want to."
    p "Alright, let's lock up a few slots to demonstrate this function."
    
    # 🔒 Lock 7 slots (from the end).
    $ inventory.lock_slots(7)
    # ⏳ Pause briefly to let the player notice the change.
    show screen inventory

    # ⚙️ Show inventory to see the locked slots.
    show screen inventory
    p "Kind of depressing, isn't it? After unlocking all the slots, suddenly we lock this row of slots. I'm already feeling really bad who knows how the player would react to such a thing. Crazy, isn't it?"
    p "Well, we demonstrated our lock 🔓 function. The thing is, I'm a bit of a softy, so I'm going to unlock the slots even though it's just a tutorial."
    # 🔓 Unlock those 7 slots again.
    $ inventory.unlock_slots(7)

    p "That sweet, magical unlocking sound. It's like an instant chill pill for my brain. Ah, much better now!"
    show screen inventory
    p "Alright, we've talked a lot about slots. You're probably tired of hearing about them by now. I promise this is the last time I'll mention slots."
    # ⚙️ Show inventory one more time for the slot discussion.
    
    show screen inventory
    p "If you think about it, the default 21 slots might not cut it for your game. So, what do you do in such a scenario? Don't sweat it, we've got a function for that too!"
    show screenshot_7
    
    p "If you're worried that adding more slots will make the inventory grid explode from lack of space, fear not! Ren'Py's got your back with a handy scroll bar that will magically manage it all."
    p "It's already built into your screen code and ready to handle any number of slots. Just add more slots, and watch the scroll bar spring into action!"
    p "As always, we need to call the `increase_slot_count` function. In the parameter, we define the number of slots we want to include."
    # ✨ Increase the *total* number of slots the inventory can hold by 21.
    # We had 21, now we'll have 21 + 21 = 42 potential slots (though they might start locked).
    $ inventory.increase_slot_count(21)
    # ⏳ Short pause.
    pause 0.5

    hide screenshot_7
    # ⚙️ Show inventory to see the increased total slot count (likely with a scrollbar now).
    show screen inventory
    
    p "We've got seven slots per row, so I figured, why settle for one row when you can have three? Bam! 21 extra slots, just like magic. Give that scroll bar a little wiggle and behold the glory."
    p "I *barely* resisted the urge to add an infinite scroll. Now it's your turn to fight the madness. If you feel brave, crank up the `increase_slot_count` function. But don't blame me if you get lost in slot-adding euphoria!"
    p "Alright, if my brain isn't completely fried, I think I've covered all the functionalities. Sooo… this should be the end of our glorious little tutorial!"
    p "Since we're wrapping up, I feel like I should say something heartfelt. Y'know, leave you with a warm fuzzy feeling or whatever. But I'm about as good at goodbyes as a cat is at swimming, so… here goes nothing."
    p "They say all good things must come to an end… which is kind of rude, honestly. But hey, I guess this is goodbye. Have fun."
    p "Alrighty then, good luck with your project. I'm signing off now like a dramatic movie character walking into the sunset."
    
    show Grassland_sunset 
    
    p "For some reason, I can't shake the feeling that I've forgotten something. At this rate, forgetting things is becoming my new hobby. Impressive, isn't it?"
 
    p "Wait… hold up. Why do I suddenly feel like I left the oven on… but for *code*?" with hpunch
    p "Before I vanish into the digital abyss, lemme just do one last paranoid double-check. Y'know, for 'safety reasons'… and so you don't come back yelling, 'YOU FORGOT FUNCTION XYZ!!' in the comments."
    p "Oops!! Aha! There it is the most important function in this whole inventory system. THE ITEM ACTION FUNCTION. Yeah. Kinda a big deal. Can't believe I almost forgot it."
    p "Before I explain how it works, let me tell you *why* it's so important. Imagine you've just integrated this inventory system into your struggling winter survival game. Everything looks great, right? Slots, scrollbars, fruits… cozy."
    p "But wait… now what? Your inventory works, sure, but… what's the *point* if you can't do anything with the items? That's where action events come in."
    p "And by action events, I mean this: if a certain item is in your inventory, you want to *do* something. Like, trigger an event. Jump to a label. Launch a cutscene. Start a romantic subplot involving a magical pomegranate. Whatever."
    p "Basically: `has_item() → if True → do cool stuff`. That's the vibe."
    p "Now here's the tricky part: this system is meant to be neutral designed for *everyone*. So I can't just throw in a specific 'use item' function or lock it to a certain character type. I mean, what if you're using a totally different character system?"
    p "For example: if I built it around an custom object-oriented character class, it might break for folks using the default Ren'Py setup like the good ol' Eileen-style global character variable from the starter tutorial."
    p "And I know many of you are gonna want at least these three actions: 1) Use Item, 2) Consume Item, and 3) Trigger Event (aka jump to a label). Bonus points if it can also boost affection with someone. Maybe even unlock a secret boss fight. Who knows."
    p "But again, everyone's setup is different. Some of you are writing massive RPGs. Others are making cozy slice-of-life games where you romance sentient sandwiches. So, instead of forcing a rigid function on you..."
    p "I built a flexible function. The idea is super simple: use `has_item()` to check if an item exists in the inventory, then use normal control flow like `if`, `elif`, `else` to trigger whatever custom behavior you want."

    p "That way, you can keep using your existing character setup, whether it's a fancy custom object-oriented class or just a Classic Ren'py character setup."
    p "And yes, this is the classic 'chicken-side-method' of scripting. Why? Because it's reliable. It's safe. And most importantly it works with *anything*."
    p "As long as `has_item()` returns true, you can do literally whatever you want: remove the item, jump to a scene, update stats, fall in love with a banana sky's the limit."
    
    show screenshot_8
    
    p "Here's an example from the tutorial project. See how the script checks for items using `has_item()` and then jumps to a specific label? That's it. That's the magic."
    p "If you go back to the `Item_actions` section in `script.rpy`, you'll see how I created custom actions for different items. It's all simple `if/else` logic super readable, super moddable."
    p "And if you're wondering, 'But what about a Use Item function? Or a function that boosts health, or affection?' Well, you've got two options:"
    p "Option 1: Write your own custom function inside the source code based on your game's specific needs."
    p "Option 2: Be smart about it. Use `has_item()` in a condition, then manually call `remove_item()` *and* update your stats or variables right there in the script."
    p "Like: `if inventory.has_item('Potion'): inventory.remove_item('Potion'); health += 20` boom. Instant heal. No drama."
    p "Let me walk you through it real quick so you're not staring at it like 'uhhh… why am I jumping into banana world?'"
    p "Here's what happens: we use the `has_item()` function to check whether the player has a certain item like an Apple or an Orange."
    p "Depending on what we've got in our inventory, we'll jump to a specific label and show them a custom response. It's like fruit-based branching dialogue. Juicy, right?"
    p "Right now, I've set it up to check for Apple, Orange (specifically 2 of them), but we have all these fruits."
    
    hide screenshot_8
    
    p "But hold on I know what you're thinking: 'Wait! I also saw Strawberry, Peach, and Pear in the project! What about those fruits? "
    p "In the main script.rpy file, I already created labels for those fruits, so you can experiment with the other fruits later and have some fun."
    
    # ⚙️ Show inventory so the player sees what items trigger the actions.

    show screen inventory

    p "But first, let's take a look at the inventory screen! This way, you'll see exactly what the player has and what we're about to check."
    p "For the purpose of this example, we'll use the fruit items you can see here in the inventory. Not the most original choice, I know, but they're perfect for walking you through this tutorial."
    p "Our next step is to jump to the item interaction logic."
    p "This is where we'll use our 'has item' function to figure out which specific action or path we need to jump to based on the player's inventory."
    p "If you're feeling a bit confused at any point, no worries! You can always check the complete tutorial project code to make more sense of how it all fits together."
    p "Alright, alright, let's head over to that item interaction section now and see how things work based on those inventory items!"
    p "For the sake of example, we’re cooking up a bunch of scenarios based on the inventory items. Let’s dive in!"
    # 👉 Jump to the section that handles item actions.
    jump Item_actions

# 💾 Initialize persistent flags to track if item messages have been shown.
# This stops the same message from popping up every time we check the inventory.
default apple_label = False
default orange_label = False
default pomegranate_label = False
default banana_label = False
default kiwi_label = False

# =============================
# == 🍎 Item Actions Logic ==
# =============================
label Item_actions:
    # -------------------------------------------------------------------------
    # ► Control Flow Explanation:
    # This label checks the inventory for specific items.
    # It uses 'if/elif/else' to check in a specific order (priority).
    # Once an item check is TRUE and its flag is FALSE, it jumps to that item's label.
    # After the item label finishes (using 'jump Item_actions'), it comes back HERE to check again.
    # This allows handling multiple items over time without getting stuck.
    # The 'and not [fruit]_label' part prevents showing the same message repeatedly.
    # -------------------------------------------------------------------------

    # ✅ CHECK 1: Apple (Highest Priority)
    # Do we have *any* Apples AND haven't shown the Apple message yet?
    if inventory.has_item("Apple") and not apple_label:
        show screen inventory # Show inventory contextually
        # Dialogue triggering the Apple event:
        "Suddenly, the ground trembles!" with vpunch
        "A ghostly voice echoes..."
        "You dare carry the Crimson Apple? You shall be sent to the **Apple Road!**"
        $ apple_label = True  # Mark Apple message as shown
        hide screen inventory
        jump apple_label      # Go to Apple-specific dialogue, then RETURN here naturally

    # ✅ CHECK 2: Oranges (Requires *at least* 2)
    # Do we have 2 or more Oranges AND haven't shown the Orange message?
    elif inventory.has_item("Orange", 2) and not orange_label:
        show screen inventory
        # Dialogue triggering the Orange event:
        p "More than two oranges? That's dangerously close to smoothie territory!"
        $ orange_label = True # Mark Orange message as shown
        hide screen inventory
        jump orange_label     # Go to Orange-specific dialogue, then RETURN here

    # ✅ CHECK 3: Pomegranate
    elif inventory.has_item("Pomegranate") and not pomegranate_label:
        show screen inventory
        # Dialogue triggering the Pomegranate event:
        p "A Pomegranate? Bold choice. Are you summoning ancient fruit spirits or just planning a very fancy breakfast?"
        $ pomegranate_label = True # Mark Pomegranate message as shown
        hide screen inventory
        jump pomegranate_label

    # ✅ CHECK 4: Banana
    elif inventory.has_item("Banana") and not banana_label:
        show screen inventory
        # Dialogue triggering the Banana event:
        p "A Banana?! Careful one slip and your whole inventory might collapse."
        $ banana_label = True # Mark Banana message as shown
        hide screen inventory
        jump banana_label

    # ✅ CHECK 5: Kiwi
    elif inventory.has_item("Kiwi") and not kiwi_label:
        show screen inventory
        # Dialogue triggering the Kiwi event:
        p "A Kiwi? Someone's got taste. And a spoon, hopefully."
        $ kiwi_label = True   # Mark Kiwi message as shown
        hide screen inventory
        jump kiwi_label

    # ✨ SPECIAL CASE: Progress when *both* apple and orange messages have been shown.
    elif apple_label and orange_label:
        # Dialogue for reaching the conclusion state:
        p "Looks like we've triggered both the Apple and Orange events. That's the main flow we wanted to demonstrate!"
        p "This concludes the item interaction part of the tutorial."
        jump goodbye          # All required checks done, exit this loop.

    # ❓ FALLBACK: No specific items found (or messages already shown).
    else:
        # Dialogue when none of the specific item conditions are met:
        p "Okay, looks like we don't have any of the specific items we're checking for right now, or their messages have already been shown."
        p "No special fruit events triggered this time based on the current checks."
        jump fruitless_label # Go to the 'empty' dialogue, then RETURN here

    return # Technically not reached after jump

# ==============================
# == 🍇 Example Fruit Labels ==
# ==============================
# 💡 These labels contain the dialogue specific to each fruit.
# After the dialogue, they usually 'jump Item_actions' to re-check the inventory.

label apple_label:
    scene apple_road with fade
    # Dialogue for the Apple event (continued from Item_actions):
    "Before you can protest, reality bends... and you find yourself in a vast orchard filled with shimmering apples."
    "Welcome, traveler. Your fate is now intertwined with the fruit!"
    # 👉 Going back to the Item_actions label to re-check the inventory state.
    p "Okay, that was the Apple event!  Awesome let's jump into the orange label because we have more than two oranges." # Added clear transition text
    jump Item_actions
    return # Technically not needed after jump

label orange_label:
    # Dialogue for the Orange event:
    scene Orange_road with dissolve
    p "Wow, we have multiple oranges! Your vitamin C levels are going to hit superhero status, isn't it amazing?" # Changed "ten" to "multiple" to align with check
    p "Try not to juggle them unless you're ready for a sticky disaster."
    # Removed the confusing tutorial explanation and conclusion from here.
    # 👉 Going back to the Item_actions label to re-check the inventory state.
    p "Alright, enough orange-ing around. Let's peel ourselves back to the item checks!" # Added clear transition text
    jump Item_actions
    return # Technically not needed after jump

label pomegranate_label:
    # Dialogue for the Pomegranate event:
    p "This is a Pomegranate. A fruit, a puzzle, and a personality test."
    p "Warning: May stain fingers, souls, and clothing."
    # 💡 To re-check inventory after this, add: jump Item_actions
    # Added dialogue cue before jump:
    p "Alright, now that we've acknowledged the Pomegranate, let's check the inventory again."
    jump Item_actions
    return

label banana_label:
    # Dialogue for the Banana event:
    p "Banana: the most comedic of fruits. Use responsibly."
    p "Fun fact: Works great as a phone if you're lonely."
    # 💡 To re-check inventory after this, add: jump Item_actions
    # Added dialogue cue before jump:
    p "Okay, joke's over. Back to checking the inventory for other reactions!"
    jump Item_actions
    return

label kiwi_label:
    # Dialogue for the Kiwi event:
    p "You picked a Kiwi. You're either a culinary genius or a fruit hipster. Or both."
    p "Spoon optional. Style points mandatory."
    # 💡 To re-check inventory after this, add: jump Item_actions
    # Added dialogue cue before jump:
    p "Interesting... a Kiwi. Let's see if anything else in the inventory triggers a reaction."
    jump Item_actions
    return

label fruitless_label:
    # Dialogue when no specific item checks pass:
    p "Right now, your inventory doesn't contain any of the specific items we're checking for that haven't already triggered their event." # More precise and less negative
    p "No special fruit events triggered this time based on the current checks."
    # 👉 Going back to the Item_actions label (maybe the player got an item?).
    p "We'll loop back to the item checker now, in case something changed, or to move on if the necessary conditions are met." # Added clear transition text explaining the loop
    jump Item_actions
    return # Technically not needed after jump

# Assuming 'goodbye' label exists elsewhere and marks the end of this section or tutorial part.
# label goodbye:
#    p "Tutorial conclusion."
#    return

# ======================
# == 👋 End of Tutorial ==
# ======================
label goodbye:
    p  "Looks like we've come to the end of the journey! The grand finale is here, Thank you for sticking with me through all the fun and craziness it's been a blast!"
    p "If you liked this tutorial, I'd be over the moon (and a couple stars) if you gave me a shout-out. I poured my pixelated heart into this."
    p "Wanna see more of my random creative mess? I've got stuff on GitHub and Itch.io. Come poke around who knows, you might find something cool or weird (or both)."
    p "Spotted a bug? Got an idea? Want to write angry poetry about the scrollbar? Drop me a GitHub issue. I love hearing from fellow tinkerers."
    p "Alright, best of luck with your game. May your code be bug-free, your assets be optimized, and your players cry happy tears."
    p "Okay, Patchmonk signing off. For real this time. Probably. Maybe."
    # 🎬 Tutorial complete!
    return