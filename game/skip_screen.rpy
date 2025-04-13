# #################################################################################################################
# #██████╗ ███████╗██████╗ ██████╗ ██╗   ██╗     ██████╗        ██████╗ ███████╗███╗   ██╗██████╗ ███████╗██████╗ #
# #██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝    ██╔════╝        ██╔══██╗██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗#
# #██████╔╝█████╗  ██████╔╝██████╔╝ ╚████╔╝     ██║  ███╗       ██████╔╝█████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝#
# #██╔══██╗██╔══╝  ██╔══██╗██╔══██╗  ╚██╔╝      ██║   ██║       ██╔══██╗██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗#
# #██████╔╝███████╗██║  ██║██║  ██║   ██║       ╚██████╔╝██╗    ██████╔╝███████╗██║ ╚████║██████╔╝███████╗██║  ██║#
# #╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝        ╚═════╝ ╚═╝    ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝#
# #################################################################################################################
###############################################################################################################################
## skip_screen.rpy ########################################################################################################################
##
## The skipscreen functionality in Ren'Py is a simple yet effective way to enhance player experience by providing an option to skip content. 
## By understanding the structure andpurpose of the code, you can easily implement similar features in your own visual novels. 
## This not only makes your game more user-friendly but also allows players to engage with the story in a way that suits their preferences. 
## The line action MainMenu(False) is particularly important. It defines what happens when the "Skip" button is clicked. 
## MainMenu: This is a built-in Ren'Py function that takes the player to the main menu of the game. False: The argument False indicates that 
## the game should not save the current state before returning to the main menu. 
## This means that any progress made in the current session will be lost, which is typically the desired behavior for a skip function.
## In summary, this line effectively allows players to exit the current game session and return 
## to the main menu without saving, providing a clean break from the ongoing narrative.
############################################################################################################################################
screen scrSkip():
    
    textbutton "Skip" align(.95, .95) action MainMenu(False)