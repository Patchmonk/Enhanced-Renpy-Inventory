# close icon 
image close:
    "components/inventory_system/images/gui/close.png"
    size(30,30) 
    
image close_hover:
    "components/inventory_system/images/gui/close_hover.png"
    size(30,30) 

style inventory_frame is frame:
    xalign 0.5
    yalign 0.3
    xsize 1180
    ysize 600
    background "components/inventory_system/images/gui/Inventory_frame_BG.png"

style close_btn:
    xpos 1135
    ypos 3
    
style inventory_title:
    size 40
    pos (0, -40)
    color Color((222, 222, 222, 255))
style dummy is text:
    size 6

style inventory_container is vbox:
    xpos 30
    ypos 50

style inventory_grid is vpgrid:
    spacing 5
   
style inventory_scrollbar is scrollbar: 
    xsize 1105
    ysize 450
 
style inventory_item_name is text:
    size 14
    bold True
    color Color((251, 251, 251, 255))
    pos (2,0)
 

style inventory_item_quantity is text:
    size 12
    bold True
    color Color((251, 251, 251, 255))
    text_align 1.0
    pos (135, 135)
    xanchor 1.0
    yanchor 1.0
 
style hud_frame is frame:
    xpadding 10
    ypadding 10
    xalign 0.5
    yalign 0.0

 
 