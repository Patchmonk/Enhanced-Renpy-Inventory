###################################################################################################################
# ██████╗  █████╗ ████████╗ ██████╗██╗  ██╗███╗   ███╗ ██████╗ ███╗   ██╗██╗  ██╗                                 #
# ██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║  ██║████╗ ████║██╔═══██╗████╗  ██║██║ ██╔╝                                 #
# ██████╔╝███████║   ██║   ██║     ███████║██╔████╔██║██║   ██║██╔██╗ ██║█████╔╝                                  #
# ██╔═══╝ ██╔══██║   ██║   ██║     ██╔══██║██║╚██╔╝██║██║   ██║██║╚██╗██║██╔═██╗                                  #
# ██║     ██║  ██║   ██║   ╚██████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝██║ ╚████║██║  ██╗                                 #
# ╚═╝     ╚═╝  ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝                                 #
###################################################################################################################
###################################################################################################################
## The inventory screen code is a well-structured way to manage and display items within a game.                  #
## By utilizing various screen elements like frames, boxes,  it creates an interactive experience for players.    #
## Understanding this code can help you customize your own inventory systems, enhancing the gameplay experience.  #
## ################################################################################################################

screen scrInventory():
    modal True  # Makes the inventory screen modal
    frame:
        style "inventory_frame"  # Applies a style to the frame
        hbox:  # Horizontal box for layout
            imagebutton:
                style "close_btn"  # Style for the close button
                idle "closebtn"  # Image when idle
                hover "closebtn_hover"  # Image when hovered
                action [Play("audio", "components/notification/audio/inventory_close.ogg"), Hide("scrInventory")]  # Action on click to hide the inventory when clicked, audible

# ####################################################################################
# #  █████╗ ██████╗ ██████╗     ████████╗ ██████╗  ██████╗ ██╗  ████████╗██╗██████╗  #
# # ██╔══██╗██╔══██╗██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║  ╚══██╔══╝██║██╔══██╗ #
# # ███████║██║  ██║██║  ██║       ██║   ██║   ██║██║   ██║██║     ██║   ██║██████╔╝ #
# # ██╔══██║██║  ██║██║  ██║       ██║   ██║   ██║██║   ██║██║     ██║   ██║██╔═══╝  #
# # ██║  ██║██████╔╝██████╔╝       ██║   ╚██████╔╝╚██████╔╝███████╗██║   ██║██║      #
# # ╚═╝  ╚═╝╚═════╝ ╚═════╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚═╝   ╚═╝╚═╝      #
# #################################################################################### A
# Step 1: Initialize a tooltip with an empty string This line creates a default tooltip object named tooltip_text. Initially, it is set to an empty string, meaning no tooltip will be displayed until we assign a value to it.
            default tooltip_text = Tooltip("")
            text __(tooltip_text.value) size 14 xpos 0.8 ypos 0.0 xmaximum 800 xfill True # Display text on the screen The text will show the value of tooltip_text when hovered over. The __ function is used to translate the tooltip text


        vbox:  # Vertical box for stacking elements
            style "inventory_container"
            text "" xpos 0.0 ypos 0.0 style "inventory_title"  # Title of the inventory, currently a placeholder
            viewport id "vp":  # Viewport for scrolling
                ysize 475
                draggable False
                mousewheel True
                scrollbars "vertical"
                vscrollbar_xsize 8
                vscrollbar_ysize 470
                vscrollbar_ypos 0
                vscrollbar_xpos -37
                vscrollbar_base_bar "components/inventory_system/images/gui/inv_vscrollbar_base_bar.png"
                vscrollbar_thumb "components/inventory_system/images/gui/inv_vscrollbar_thumb.png"
                vscrollbar_unscrollable "hide"
                vpgrid cols 7:  # Grid layout for inventory slots, 7 in a row
                    style "inventory_grid"
                    for slot in range(inventory.slot_count):  # Loop through each inventory slot
                        frame:
                            xsize 155  # Size of the frame, creating space between items
                            ysize 155
                            if inventory.is_slot_unlocked(slot):  # Check if the slot is unlocked
                                background "components/inventory_system/images/gui/slot_bg.png"  # Background for unlocked slot
                                if inventory.slots[slot]:  # Check if there is an item in the slot
                                    for item, quantity in inventory.slots[slot].items():  # Loop through items in the slot

# ####################################################################################
# #  █████╗ ██████╗ ██████╗     ████████╗ ██████╗  ██████╗ ██╗  ████████╗██╗██████╗  #
# # ██╔══██╗██╔══██╗██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║  ╚══██╔══╝██║██╔══██╗ #
# # ███████║██║  ██║██║  ██║       ██║   ██║   ██║██║   ██║██║     ██║   ██║██████╔╝ #
# # ██╔══██║██║  ██║██║  ██║       ██║   ██║   ██║██║   ██║██║     ██║   ██║██╔═══╝  #
# # ██║  ██║██████╔╝██████╔╝       ██║   ╚██████╔╝╚██████╔╝███████╗██║   ██║██║      #
# # ╚═╝  ╚═╝╚═════╝ ╚═════╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚═╝   ╚═╝╚═╝      #
# #################################################################################### B
# Step 2: Here, we are creating a dynamic string that will hold the translated value of item. The f before the string indicates that it is an f-string, allowing for easy variable interpolation.
                                        $ tooltip_string = f"{__(item)}"


# #################################################################################################################################################################################################################################
# #  █████╗ ██████╗ ██████╗     ██╗███╗   ███╗ █████╗  ██████╗ ███████╗██████╗ ██╗   ██╗████████╗████████╗ ██████╗ ███╗   ██╗    ███████╗ ██████╗ ██████╗     ███████╗ █████╗  ██████╗██╗  ██╗    ██╗████████╗███████╗███╗   ███╗ #
# # ██╔══██╗██╔══██╗██╔══██╗    ██║████╗ ████║██╔══██╗██╔════╝ ██╔════╝██╔══██╗██║   ██║╚══██╔══╝╚══██╔══╝██╔═══██╗████╗  ██║    ██╔════╝██╔═══██╗██╔══██╗    ██╔════╝██╔══██╗██╔════╝██║  ██║    ██║╚══██╔══╝██╔════╝████╗ ████║ #
# # ███████║██║  ██║██║  ██║    ██║██╔████╔██║███████║██║  ███╗█████╗  ██████╔╝██║   ██║   ██║      ██║   ██║   ██║██╔██╗ ██║    █████╗  ██║   ██║██████╔╝    █████╗  ███████║██║     ███████║    ██║   ██║   █████╗  ██╔████╔██║ #
# # ██╔══██║██║  ██║██║  ██║    ██║██║╚██╔╝██║██╔══██║██║   ██║██╔══╝  ██╔══██╗██║   ██║   ██║      ██║   ██║   ██║██║╚██╗██║    ██╔══╝  ██║   ██║██╔══██╗    ██╔══╝  ██╔══██║██║     ██╔══██║    ██║   ██║   ██╔══╝  ██║╚██╔╝██║ #
# # ██║  ██║██████╔╝██████╔╝    ██║██║ ╚═╝ ██║██║  ██║╚██████╔╝███████╗██████╔╝╚██████╔╝   ██║      ██║   ╚██████╔╝██║ ╚████║    ██║     ╚██████╔╝██║  ██║    ███████╗██║  ██║╚██████╗██║  ██║    ██║   ██║   ███████╗██║ ╚═╝ ██║ #
# # ╚═╝  ╚═╝╚═════╝ ╚═════╝     ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═════╝  ╚═════╝    ╚═╝      ╚═╝    ╚═════╝ ╚═╝  ╚═══╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚═╝   ╚═╝   ╚══════╝╚═╝     ╚═╝ #
# #################################################################################################################################################################################################################################
                                        imagebutton:
                                            style "inv_item_btn"
                                            idle "components/inventory_system/images/icons/" + item + ".png"  # Item icon
                                            hover "components/inventory_system/images/icons/" + item + "_hover.png"  # Hover icon

# ####################################################################################
# #  █████╗ ██████╗ ██████╗     ████████╗ ██████╗  ██████╗ ██╗  ████████╗██╗██████╗  #
# # ██╔══██╗██╔══██╗██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║  ╚══██╔══╝██║██╔══██╗ #
# # ███████║██║  ██║██║  ██║       ██║   ██║   ██║██║   ██║██║     ██║   ██║██████╔╝ #
# # ██╔══██║██║  ██║██║  ██║       ██║   ██║   ██║██║   ██║██║     ██║   ██║██╔═══╝  #
# # ██║  ██║██████╔╝██████╔╝       ██║   ╚██████╔╝╚██████╔╝███████╗██║   ██║██║      #
# # ╚═╝  ╚═╝╚═════╝ ╚═════╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚═╝   ╚═╝╚═╝      #
# #################################################################################### C
# Step 3:   The hovered tooltip_text.Action(t_text) part specifies that when the user hovers over the button, the tooltip defined in tooltip_string will appear.
                                            hovered tooltip_text.Action(tooltip_string)

# ###############################################################################
# #  █████╗ ██████╗ ██████╗      █████╗  ██████╗████████╗██╗ ██████╗ ███╗   ██╗ #
# # ██╔══██╗██╔══██╗██╔══██╗    ██╔══██╗██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║ #
# # ███████║██║  ██║██║  ██║    ███████║██║        ██║   ██║██║   ██║██╔██╗ ██║ #
# # ██╔══██║██║  ██║██║  ██║    ██╔══██║██║        ██║   ██║██║   ██║██║╚██╗██║ #
# # ██║  ██║██████╔╝██████╔╝    ██║  ██║╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║ #
# # ╚═╝  ╚═╝╚═════╝ ╚═════╝     ╚═╝  ╚═╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ #
# ################################################################################
# Action on click, for now it would play the file item.mp3 and show the item.rpy file  i.e. apple.mp3 and apple.rpy, quite useless but it's a start TODO: meaningful actions
                                            action [Play("audio", item + ".mp3"), Show(item)]


# ##################################################################################################################
# #  █████╗ ██████╗ ██████╗     ██████╗ ███████╗███████╗ ██████╗██████╗ ██╗██████╗ ████████╗██╗ ██████╗ ███╗   ██╗ #
# # ██╔══██╗██╔══██╗██╔══██╗    ██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗██║██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║ #
# # ███████║██║  ██║██║  ██║    ██║  ██║█████╗  ███████╗██║     ██████╔╝██║██████╔╝   ██║   ██║██║   ██║██╔██╗ ██║ #
# # ██╔══██║██║  ██║██║  ██║    ██║  ██║██╔══╝  ╚════██║██║     ██╔══██╗██║██╔═══╝    ██║   ██║██║   ██║██║╚██╗██║ #
# # ██║  ██║██████╔╝██████╔╝    ██████╔╝███████╗███████║╚██████╗██║  ██║██║██║        ██║   ██║╚██████╔╝██║ ╚████║ #
# # ╚═╝  ╚═╝╚═════╝ ╚═════╝     ╚═════╝ ╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ #
# ##################################################################################################################
# Step 1: Create a list of fruits and cats so we can categorize the items into fruit cats and so on
                                        $ healthy_fruits = ["apple", "banana", "lemon", "orange", "grape", "kiwi", "mango", "peach", "pear", "plum", "cherry", "strawberry", "blueberry", "raspberry", "watermelon", "pineapple", "papaya", "cantaloupe", "fig", "pomegranate"]
                                        $ art_cats = ["cat01", "cat02", "cat03", "cat04", "cat05", "cat06", "cat07", "cat08"]



                                        $ Inv_item_name = item.replace('_', ' ')  # Format item name
                                        $ Inv_item_quantity = f"x{quantity}"  # Format item quantity

                                        text Inv_item_name style "inventory_item_name"  # Add item name upper left of frame
                                        text Inv_item_quantity style "inventory_item_quantity"  # Add item quantity lower right of frame
# ##################################################################################################################
# #  █████╗ ██████╗ ██████╗     ██████╗ ███████╗███████╗ ██████╗██████╗ ██╗██████╗ ████████╗██╗ ██████╗ ███╗   ██╗ #
# # ██╔══██╗██╔══██╗██╔══██╗    ██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗██║██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║ #
# # ███████║██║  ██║██║  ██║    ██║  ██║█████╗  ███████╗██║     ██████╔╝██║██████╔╝   ██║   ██║██║   ██║██╔██╗ ██║ #
# # ██╔══██║██║  ██║██║  ██║    ██║  ██║██╔══╝  ╚════██║██║     ██╔══██╗██║██╔═══╝    ██║   ██║██║   ██║██║╚██╗██║ #
# # ██║  ██║██████╔╝██████╔╝    ██████╔╝███████╗███████║╚██████╗██║  ██║██║██║        ██║   ██║╚██████╔╝██║ ╚████║ #
# # ╚═╝  ╚═╝╚═════╝ ╚═════╝     ╚═════╝ ╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ #
# ##################################################################################################################
# Step 2: Check whether we have fruit, or cats
# Step 3: And add the description to the frame lowerleft (style references)
                                        if Inv_item_name in healthy_fruits:
                                            text "Fruit" style "inventory_item_description"
                                        elif Inv_item_name == "these":
                                            text "Persian" style "inventory_item_description"
                                        elif Inv_item_name == "are":
                                            text "Birman" style "inventory_item_description"
                                        elif Inv_item_name == "all":
                                            text "Burmese" style "inventory_item_description"
                                        elif Inv_item_name == "beautiful":
                                            text "Ragdoll" style "inventory_item_description"
                                        elif Inv_item_name == "and":
                                            text "Devon" style "inventory_item_description"
                                        elif Inv_item_name == "cute":
                                            text "Shorthair" style "inventory_item_description"
                                        elif Inv_item_name == "little":
                                            text "Bengal" style "inventory_item_description"
                                        elif Inv_item_name == "cats":
                                            text "Maine" style "inventory_item_description"    
                                        elif Inv_item_name == "diamond":
                                            text "Wealth" style "inventory_item_description"                        

                            else:
                                background "components/inventory_system/images/gui/locked_slot_bg.png"  # Background for locked slot
