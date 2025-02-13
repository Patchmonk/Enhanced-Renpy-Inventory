# Enhanced-Renpy-Inventory  

This project builds upon my previous work, [Simple Ren'Py Inventory](https://github.com/Patchmonk/Simple-Renpy-Inventory?tab=readme-ov-file#simple-renpy-inventory), which was straightforward and beginner-friendly but missed some advanced features that many games use today. So, I decided to level it up with this version, making it both simple enough for beginners and advanced enough for anyone who wants to get fancy with customization.  

This system is designed with flexibility and dynamism in mind, allowing for effective item and slot management. Players can store, organize, and interact with items while also incorporating progression mechanics, like unlocking additional inventory slots as the game moves forward. It’s built for scalability, so whether you’re making a chill visual novel, a dating sim, or even a complex RPG, this should do the trick.  

Oh, and about the tutorial... Listen, I'm not a tutorial wizard, but I tried my best to make the learning process less boring. You’ll find a step-by-step guide embedded in the visual novel itself, complete with some attempts at humor. I can’t promise it’s funny I mean, you’ll probably cringe at a few lines but hey, I did my best to keep it interesting. No promises on it being a cool Step-by-step walkthrough. It's just a tutorial with a little personality, that’s all.  
 



## Key Features 🚀

- **In-Game Tutorial**  
  I’m not saying it’s the best tutorial out there, but... well, I tried. It's a step-by-step guide on how to use the inventory system, and I added a bit of dialogue to keep it... *interesting.* So, give it a try, and if you find yourself cringing at any of the jokes, I totally understand.  

- **Dynamic Slot Management**  
  - Adjust your inventory size with ease. You can unlock and lock slots as needed.  
  - Need more space? Use the `increase_slot_count()` function to expand your inventory.  

- **Smart Item Handling**  
  - Items stack with a max limit per slot, and the inventory auto-sorts after you remove items.  
  - Custom notifications to keep you informed about the good and the bad.  

- **Customizable System**  
  - Perfect for any type of Ren'Py game, whether you’re making a simple dating sim or a complex RPG.  

 

## Why Use This System? 🧐  
This inventory system is designed to be easy to use, flexible, and (hopefully) not too tedious to learn, thanks to the tutorial. I can’t promise it’ll be a life-changing experience, but it *should* make inventory management in your Ren'Py project a lot smoother.  

 

## Installation & Integration ⚙️  
1. Copy the Python class into your Ren'Py project.  
2. Adjust the slot count and item settings to your liking.  
3. Open the game and let the tutorial walk you through everything (or laugh... or cringe).  

 

## How to implement this system? 💻  
```renpy


# Inventory initialization
default inventory = Inventory(slot_count=21, unlocked_slots=7)


# The start of the game
label start:

# Add Items
$ inventory.add_item("Potion", 3)
$ inventory.add_item("Sword", 1)

# Remove Items
$ inventory.remove_item("Potion", 1)

# Unlock Slots
$ inventory.unlock_slots(3)

# Increase Slot Capacity
$ inventory.increase_slot_count(5)


```

 

## Compatibility & Requirements 🛠️
- **Engine**: Ren'Py (Tested on version 8.0 and above)  
- **Language**: Python (Integrated with Ren'Py scripting)

 
 

## Why This Exists: 🤔 
I’ve always found it weird that so many GitHub repos don’t have proper descriptions or tutorials. I mean, what's the point of sharing code if nobody knows how to use it? That’s why I made this inventory system easy to understand, with a tutorial that actually explains how it works step by step. Sure, I tried to make it a little fun, It’s just a friendly guide that’s more interesting than plain documentation.  

 

## A Final Word from Me 💬  
I put in a fair amount of work creating this system. But when it came to the tutorial, let’s just say I was *really* hoping you’d find it helpful (and not too embarrassing). 😅 I mean, I don't have a lot of confidence in my humor, but if it helps you understand how to use this system, then I’ll call it a win! Enjoy, and don't hesitate to reach out if something doesn't make sense. Or if you have any brilliant ideas to take this system to the next level, I'm all ears! (Or if you just want to tell me how bad my jokes are). Cheers!
 
