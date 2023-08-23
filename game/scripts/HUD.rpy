screen HUD():
    frame:
        xpos 0 ypos 0
        xminimum 1920
        yminimum 100
        has hbox
        
        # Display the weekday, time of day, and current hours
    
        text " Gold : [gold]" xpos 10 ypos 20 
        imagebutton:
            xpos 0 ypos 0
            idle "Backpack"
            hover "Backpack_Hover"
            action Show("inventoryScreen")
            padding (10, 10, 10, 10)

image Backpack:
    "images/inventory/inventory_gui/backpack.png"
    size(60,60) 

# backpack icon     
image Backpack_Hover:
    "images/inventory/inventory_gui/backpack_hover.png"
    size(60,60) 

image close:
    "images/inventory/inventory_gui/close.png"
    size(30,30) 

# backpack icon     
image close_hover:
    "images/inventory/inventory_gui/close_hover.png"
    size(30,30) 
 