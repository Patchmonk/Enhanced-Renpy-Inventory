style inventory_frame is frame:
    xalign 0.5
    yalign 0.3
    xsize 1180
    ysize 600
    background Color((0, 0, 0, 161))

style close_btn:
    xpos 1135
    ypos 3
   
style Inv_vbox is vbox:
    align (0.5, 0.5)
  
style Inv_vbox_titel  is text:
    size 40
    align (0, 0.1)
 
style dummy is text:
    size 20
 
style Inv_grid is vpgrid:
    spacing 5
 
style inv_scrollbar is scrollbar: 
    xsize 1105
    ysize 450
 
style Inv_item_name is text:
    size 16
    bold True
    color Color((216, 0, 108, 255))
    pos (0,0)  

style Inv_item_quantity is text:
    size 16
    bold True
    color Color((216, 0, 108, 255))
    pos (0,118)  

style item_quantity is text:
    size 16
    bold True
    color Color((255, 0, 149, 255))
    pos (115,120)

style hud_frame is frame:
    xpadding 10
    ypadding 10
    xalign 0.5
    yalign 0.0

 