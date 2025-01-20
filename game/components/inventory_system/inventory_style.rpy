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
    ysize 620
    background Color((0, 0, 0, 161))

style close_btn:
    xpos 1135
    ypos 3
    
style inventory_title:
    size 40
    line_spacing 20
    
    
 
style dummy is text:
    size 6
style inventory_container is vbox:
    xpos 30
    ypos 30

style inventory_grid is vpgrid:
    spacing 5
 
style inventory_scrollbar is scrollbar: 
    xsize 1105
    ysize 450
 
style inventory_item_name is text:
    size 16
    bold True
    color Color((216, 0, 108, 255))
    pos (0,0)
 
    

style inventory_item_quantity is text:
    size 16
    bold True
    color Color((255, 0, 149, 255))
    text_align 1.0
    pos (135, 135)
    xanchor 1.0
    yanchor 1.0

 
 
style hud_frame is frame:
    xpadding 10
    ypadding 10
    xalign 0.5
    yalign 0.0

 
 