style inventory_frame is frame:
    xalign 0.5
    yalign 0.3
    xsize 1180
    ysize 580
    background Color((0, 0, 0, 161))

style close_btn:
    xpos 1135
    ypos 3
   
style inventory_titel is text:
    size 40
    line_spacing 20
    ypos 10
    
 
style dummy is text:
    size 6
style inventory_container is vbox:
    xpos 30

style inventory_grid is vpgrid:
    spacing 5
 
style inventory_scrollbar is scrollbar: 
    xsize 1105
    ysize 450
 
style inventory_item_name is text:
    size 16
    bold True
    color Color((216, 0, 108, 255))
    xalign 0.9  

 
style inventory_item_quantity is text:
    size 16
    bold True
    color Color((255, 0, 149, 255))
    pos (0,120)

style hud_frame is frame:
    xpadding 10
    ypadding 10
    xalign 0.5
    yalign 0.0

 