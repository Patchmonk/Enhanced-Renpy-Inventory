###################################################################################################################
# ██████╗  █████╗ ████████╗ ██████╗██╗  ██╗███╗   ███╗ ██████╗ ███╗   ██╗██╗  ██╗                                 #
# ██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║  ██║████╗ ████║██╔═══██╗████╗  ██║██║ ██╔╝                                 #
# ██████╔╝███████║   ██║   ██║     ███████║██╔████╔██║██║   ██║██╔██╗ ██║█████╔╝                                  #
# ██╔═══╝ ██╔══██║   ██║   ██║     ██╔══██║██║╚██╔╝██║██║   ██║██║╚██╗██║██╔═██╗                                  #
# ██║     ██║  ██║   ██║   ╚██████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝██║ ╚████║██║  ██╗                                 #
# ╚═╝     ╚═╝  ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝                                 #
###################################################################################################################
###################################################################################################################
## a foundational piece for creating an inventory system in Ren'Py. By defining images and styles,                #
## it sets up a visually appealing and functional interface for players to manage their items.                    #
## Understanding how to manipulate these styles and images will empower you to customize your inventory system    #
## further, enhancing the overall player experience in your visual novel.This style sheet has little impact on    #
## performance but it is pivotal that file paths are correct to prevent runtime errors                            #
###################################################################################################################


# Inventory frame style
style inventory_frame is frame:
    xalign 0.5
    yalign 0.3
    xsize 1180
    ysize 600
    background "components/inventory_system/images/gui/inventory_frame_bg.png"
  

# Item button style
style item_btn:
    xalign 0.5
    yalign 0.5
    focus_mask True

# Inventory close button style
style close_btn:
    xpos 1140
    ypos 3
    xsize 30
    ysize 30


# Inventory title style
style inventory_title:
    size 14
    pos (0, -40)
    color  "#00448f"

# Inventory container style
style inventory_container is vbox:
    xpos 30
    ypos 75

# Inventory grid style
style inventory_grid is vpgrid:
    spacing 5

# Inventory scrollbar style
style inventory_scrollbar is scrollbar:
    xsize 1105
    ysize 450

# Inventory item name style
style inventory_item_name is text:
    size 14
    font "art/fonts/Hacked-KerX.ttf"
    bold False
    color  "#fc8a08"
    pos (2,0)

# Inventory item quantity style
style inventory_item_quantity is text:
    size 12
    font "art/fonts/Hacked-KerX.ttf"
    bold False
    color  "#fc8a08"
    text_align 1.0 
    pos (135, 135)
    xanchor 1.0
    yanchor 1.0

# Inventory item description style
style inventory_item_description is text:
    size 12
    font "art/fonts/Hacked-KerX.ttf"
    bold False
    color  "#fc8a08"
    text_align 1.0 
    pos (0, 135)
    xanchor 0.0
    yanchor 1.0  

# Some fonts
style hacked is text:
    size 40
    font "art/fonts/Hacked-KerX.ttf"
    color "#fc8a08"
    italic False
    hover_color "#00448f"

# Some fonts
style hacked_display is text:
    size 14
    font "art/fonts/Hacked-KerX.ttf"
    color "#00448f"
    italic True
    hover_color "#fc8a08"      

# HUD frame style 
style hud_frame is frame:
    xpos 0 ypos 0 ## position frame upperleft corner
    xminimum 1920 ## horizontal size covers whole screen
    yminimum 80 ## vertical size should at least be enough for the backpack imagebutton which is 60 x 60 
    background "#0000009b" ## some shade of grey, so it is visible but doesn't cut off part of the screen entirely
    

# Define the style for the notification text
style pm_notify:
    ypos 0.3  # Position the text vertically within the frame
    xpos 135  # Position the text horizontally within the frame
    color "#00448f"  # Set the text color to black

# Define the style for the popup frame
style popup is frame:
    xsize 1400  # Set the width of the frame
    ysize 100   # Set the height of the frame
    background "components/inventory_system/images/gui/frame.png"
    xpos 0.5  # Center the frame horizontally
    ypos 0.1  # Position the frame slightly down from the top
    xanchor 0.5  # Anchor the frame to the center


# Backpack image
image Backpack:
    "components/inventory_system/images/gui/backpack.png"
    xsize 60
    ysize 60 
# Backpack hover image    
image Backpack_Hover:
    "components/inventory_system/images/gui/backpack_hover.png"
    xsize 60
    ysize 60 
# btnquit image
image quitbtn:
    "components/inventory_system/images/gui/btnquit.png"
    xsize 60
    ysize 40
# btnquit hover image
image quitbtn_hover:
    "components/inventory_system/images/gui/btnquit_hover.png"
    xsize 60
    ysize 40  
# btnamazing image
image amazingbtn:
    "components/inventory_system/images/gui/btnamazing.png"
    xsize 60
    ysize 40
# btnamazing hover image
image amazingbtn_hover:
    "components/inventory_system/images/gui/btnamazing_hover.png"
    xsize 60
    ysize 40 
# btnwork image
image workbtn:
    "components/inventory_system/images/gui/btnwork.png"
    xsize 60
    ysize 40
# btnwork hover image
image workbtn_hover:
    "components/inventory_system/images/gui/btnwork_hover.png"
    xsize 60
    ysize 40   

# btntap image
image tapbtn:
    "components/inventory_system/images/gui/btntap.png"
    xsize 60
    ysize 40  

# btntap hover image
image tapbtn_hover:
    "components/inventory_system/images/gui/btntap_hover.png"
    xsize 60
    ysize 40   

# btnplus image
image plusbtn:
    "components/inventory_system/images/gui/btnplus.png"
    xsize 60
    ysize 40

# btnplus hover image
image plusbtn_hover:
    "components/inventory_system/images/gui/btnplus_hover.png"
    xsize 60
    ysize 40    

# btnmin image
image minbtn:
    "components/inventory_system/images/gui/btnmin.png"
    xsize 60
    ysize 40

# btnmin hover image
image minbtn_hover:
    "components/inventory_system/images/gui/btnmin_hover.png"
    xsize 60
    ysize 40    

# btnclose image
image closebtn:
    "components/inventory_system/images/gui/btnclose.png"
    xsize 30
    ysize 30 
   
# btnclose hover image    
image closebtn_hover:
    "components/inventory_system/images/gui/btnclose_hover.png"
    xsize 30
    ysize 30 