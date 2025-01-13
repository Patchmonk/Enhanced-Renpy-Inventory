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

# backpack icon 
image Backpack:
    "components/inventory_system/images/gui/backpack.png"
    size(60,60) 
    
image Backpack_Hover:
    "components/inventory_system/images/gui/backpack_hover.png"
    size(60,60) 


 