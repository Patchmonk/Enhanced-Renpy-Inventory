# Patchmonk's Advanced Inventory System 1.2.7 

## #################################################################################################################################################
## The Inventory class is a robust solution for managing items in a Ren'Py game. It provides essential features such as adding and removing items, 
## dynamic slot management, and user notifications. 
## By implementing this class, developers can create a more engaging and interactive experience for players, 
## allowing them to manage their inventory effectively. 
## Whether you're building a simple game or a complex RPG, this inventory system can be a valuable addition to your project.
## #################################################################################################################################################

## #################################################################################################################################################
## The inventory screen code is a well-structured way to manage and display items within a game. 
## By utilizing various screen elements like frames, boxes, and viewports, it creates an interactive experience for players. 
## Understanding this code can help you customize your own inventory systems, enhancing the gameplay experience.
## #################################################################################################################################################

For clarification here are some of the important modifications I made: (important for me, to prevent myself from breaking the code, since I have some programming experience be it in Delphi in which case does not matter)

# Renaming
I renamed some files and screens to have them make a little bit more sense to me and following convention. I had to get rid of the
only file that required upper case (Custom_notification.rpy). I also got rid of the custom part in the notification system files. I renamed
both the notification screen and the inventory screen as well as the hud screen and renamed the files that accomodate these screens accordingly.
I.e.:
- renamed notification screen to scrNotification (notification_screen.rpy)
- renamed inventory screen to scrInventory (inventory_screen.rpy)
- renamed HUD screen to scrHud (hud_screen.rpy)
- renamed Custom_notification.rpy to notification.rpy (to get rid of that one file which required upper case)
- exception is splashscreen which can't be renamed obviously
All screens now start with prefix scr. So we have:
 - scrSkip - scrNotification - scrInventory - scrHud
These  screens are placed in the files: skip_screen.rpy, notification_screen.rpy and inventory_screen.rpy and hud_screen all lowercase.
All referenced and used files are lower case now. In game references do include uppercase.

# Commenting
I extensively commented about every move that is made, perhaps even obvious ones as well but it helped me to make sense of this code.
I added large text blocks, making it easier to see where things happen and what you need to modify and what you can disregard

# Final note
Most of the problems I encountered where related to either filepaths and usage of case, or the inventory_style.rpy file
