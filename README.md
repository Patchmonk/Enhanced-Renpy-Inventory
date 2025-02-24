# Enhanced-Renpy-Inventory  

This project builds upon my previous work, [Simple Ren'Py Inventory](https://github.com/Patchmonk/Simple-Renpy-Inventory?tab=readme-ov-file#simple-renpy-inventory), which was straightforward and beginner-friendly but lacked some advanced features that many games use today. So, I decided to level it up with this version, making it both simple enough for beginners and advanced enough for anyone who wants to get fancy with customization.  

This system is designed with flexibility and dynamism in mind, allowing for effective item and slot management. Players can store, organize, and interact with items while also incorporating progression mechanics, like unlocking additional inventory slots as the game moves forward. It’s built for scalability, so whether you’re making a chill visual novel, a dating sim, or even a complex RPG, this should do the trick.  

Oh, and about the tutorial... Listen, I'm not a tutorial wizard, but I tried my best to make the learning process less boring. You’ll find a step-by-step guide embedded in the visual novel itself, complete with some attempts at humor. I can’t promise it’s funny—I mean, you’ll probably cringe at a few lines—but hey, I did my best to keep it interesting. No promises on it being a cool step-by-step walkthrough. It's just a tutorial with a little personality, that’s all.  

![screenshot0016](https://github.com/user-attachments/assets/6d089f14-4f7c-42a9-ad57-10320d73b881)  
![screenshot0015](https://github.com/user-attachments/assets/0fd02035-040d-4ea2-8a12-1b819a67f4bb)  

---

## Key Features 🚀  

### 1. **In-Game Tutorial**  
- I’m not saying it’s the best tutorial out there, but... well, I tried. It's a step-by-step guide on how to use the inventory system, and I added a bit of dialogue to keep it... *interesting.* So, give it a try, and if you find yourself cringing at any of the jokes, I totally understand. 

- How to add and remove items.  
- How to unlock and lock inventory slots.  
- How to increase the total number of slots.  
- How the auto-sorting feature works after removing items.  

Even if you’re new to Ren'Py or inventory systems, the tutorial will walk you through everything you need to know. And yes, you might cringe at a joke or two—but hey, at least it’s memorable!  

---

### 2. **Dynamic Slot Management**  
Managing inventory slots has never been easier:  
- **Unlock Slots**: Use the `unlock_slots(count)` method to dynamically unlock additional slots during gameplay. For example, players can earn more slots as they progress through quests or levels.  
- **Lock Slots**: Use the `lock_slots(count)` method to reduce the number of unlocked slots. This could simulate penalties, such as losing access to certain slots due to in-game events.  
- **Increase Total Slots**: Use the `increase_slot_count(additional_slots)` method to expand the total number of slots available in the inventory. This is perfect for games where players can upgrade their inventory capacity.  

The system ensures that only unlocked slots are accessible for adding items, while locked slots remain inactive until unlocked.  

---

### 3. **Smart Item Handling**  
The inventory system is designed to handle items intelligently:  
- **Stacking Items**: Each slot can hold up to 99 of the same item. If you try to add more than 99 of an item, the system will automatically distribute the excess to other slots.  
- **Adding Items**: When adding items, the system first tries to stack them in existing slots with the same item. If no space is available, it places the item in the next available empty slot.  
- **Removing Items**: Use the `remove_item(item, quantity)` method to remove items from the inventory. If you remove all instances of an item from a slot, the slot becomes empty. After removal, the inventory automatically sorts itself to ensure empty slots are pushed to the end.  
- **Notifications**: Custom notifications keep players informed about actions like successfully adding or removing items, insufficient slots, or invalid quantities. These notifications can include sound effects to enhance the user experience.  

---

### 4. **Auto-Sorting Feature**  
The inventory automatically sorts itself whenever items are removed. Empty slots are moved to the end, ensuring that filled slots are always grouped together at the beginning of the inventory. This keeps the inventory organized and visually appealing without requiring manual intervention.  

---

### 5. **Customizable System**  
The inventory system is highly customizable and can be adapted to fit any type of Ren'Py game:  
- Adjust the initial number of slots and unlocked slots during initialization.  
- Modify the maximum number of items per slot (`max_items_per_slot`) to suit your game’s needs.  
- Integrate custom notifications and sound effects to match your game’s theme.  

Whether you’re building a simple dating sim or a complex RPG, this system provides the flexibility you need to create a seamless inventory experience.  

---

## Why Use This System? 🧐  
This inventory system is designed to be easy to use, flexible, and (hopefully) not too tedious to learn, thanks to the tutorial. I can’t promise it’ll be a life-changing experience, but it *should* make inventory management in your Ren'Py project a lot smoother.  

---

## Installation & Integration ⚙️  
1. Copy the Python class into your Ren'Py project.  
2. Adjust the slot count and item settings to your liking.  
3. Open the game and let the tutorial walk you through everything (or laugh... or cringe).  

---

## How to Implement This System? 💻  
```renpy
# Inventory initialization
default inventory = Inventory(slot_count=21, unlocked_slots=7)

# The start of the game
label start:
    # Add Items
    $ inventory.add_item("apple", 1)
    $ inventory.add_item("orange", 1)
    
    # Remove Items
    $ inventory.remove_item("orange", 1)
    
    # Unlock Slots
    $ inventory.unlock_slots(7)
    
    # Increase Slot Capacity
    $ inventory.increase_slot_count(7)
```

---

## Compatibility & Requirements 🛠️  
- **Engine**: Ren'Py (Tested on version 8.0 and above)  
- **Language**: Python (Integrated with Ren'Py scripting)  

---

## Why This Exists: 🤔  
I’ve always found it weird that so many GitHub repos don’t have proper descriptions or tutorials. I mean, what's the point of sharing code if nobody knows how to use it? That’s why I made this inventory system easy to understand, with a tutorial that actually explains how it works step by step. Sure, I tried to make it a little fun—it’s just a friendly guide that’s more interesting than plain documentation.  

---

## A Final Word from Me 💬  
I put in a fair amount of work creating this system. But when it came to the tutorial, let’s just say I was *really* hoping you’d find it helpful (and not too embarrassing). 😅 I mean, I don't have a lot of confidence in my humor, but if it helps you understand how to use this system, then I’ll call it a win! Enjoy, and don't hesitate to reach out if something doesn't make sense. Or if you have any brilliant ideas to take this system to the next level, I'm all ears! (Or if you just want to tell me how bad my jokes are). Cheers!
