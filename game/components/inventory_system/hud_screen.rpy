###################################################################################################################
# ██████╗  █████╗ ████████╗ ██████╗██╗  ██╗███╗   ███╗ ██████╗ ███╗   ██╗██╗  ██╗                                 #
# ██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║  ██║████╗ ████║██╔═══██╗████╗  ██║██║ ██╔╝                                 #
# ██████╔╝███████║   ██║   ██║     ███████║██╔████╔██║██║   ██║██╔██╗ ██║█████╔╝                                  #
# ██╔═══╝ ██╔══██║   ██║   ██║     ██╔══██║██║╚██╔╝██║██║   ██║██║╚██╗██║██╔═██╗                                  #
# ██║     ██║  ██║   ██║   ╚██████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝██║ ╚████║██║  ██╗                                 #
# ╚═╝     ╚═╝  ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝                                 #
###################################################################################################################
###################################################################################################################
## Creating a HUD in RenPy is a straightforward process that enhances the player's experience by providing        #
## vital information and interactive elements.                                                                    #
## The code provided demonstrates how to display the player's gold and a backpack icon that opens the inventory.  #
## By customizing the HUD, you can create a more engaging and user-friendly interface for your game.              #
###################################################################################################################
screen scrHud():
    zorder 3

    frame:
        style "hud_frame"
        has hbox ## it has an hbox  ?
        ## display the backpack including hover effect and opening sound
        imagebutton:
            xpos 0 ypos 0 ## position imagebutton upperleft corner of frame
            idle "Backpack" ## idle image
            hover "Backpack_Hover" ## hover image
            action [Play("audio", "components/notification/audio/inventory_open.ogg"),Show("scrInventory")] ## show scrInventory (audible)
            padding (20,0) ## not yet figured out
        ## display the variable "gold" , it will change during project run
        text " GOLD : [gold]" xpos 10 ypos 15 style "hacked" ## take notice of the style effect which makes the text look like images
        ## play a sound
        imagebutton idle "amazingbtn" hover "amazingbtn_hover" xpos 600 ypos 15 action [Play("audio", "audio/dream.ogg"),NullAction()]
        ## play a sound
        imagebutton idle "tapbtn" hover "tapbtn_hover" xpos 665 ypos 15 action [Play("audio", "audio/bassSuspense.ogg"),NullAction()]
        ## increase multi task level reader audible
        imagebutton idle "plusbtn" hover "plusbtn_hover" xpos 720 ypos 15 action [Play("audio", "audio/success.mp3"),Function(renpy.call, label="lbplusscore")] # ugly but works as expected
        ## decrease multi task level reader audible
        imagebutton idle "minbtn" hover "minbtn_hover" xpos 775 ypos 15 action [Play("audio", "audio/remove.mp3"),Function(renpy.call, label="lbminscore")] # ugly but works as expected
        ## display a joke and quit
        imagebutton idle "quitbtn" hover "quitbtn_hover" xpos 840 ypos 15 action Jump("lbShow_joke")
        ## display "multi_task_level_reader", it will change during project run
        text "Multitask-level reader: [multi_task_level_reader]" xpos 850 ypos 15 style "hacked"

## uses badjokes.rpy found on the internet (for providing the jokes)
label lbShow_joke:
    $ jokes = jokes_list()  # Get the list of jokes
    $ random_joke = renpy.random.choice(jokes)  # Select a random joke
    b "Here's a joke before you leave: [random_joke]"  # I'll do the dirty work ;)
    return

label lbplusscore:
    $ multi_task_level_reader = multi_task_level_reader + 50
    return


label lbminscore:
    $ multi_task_level_reader = multi_task_level_reader - 50
    return




