screen inventoryScreen():
    modal True
    frame:
        style "inventory_frame"
        imagebutton:
            style "close_btn"
            idle "close"
            hover "close_hover"
            action Hide("inventoryScreen")

        $ slot_count = inventory.slot_count
        $ slot_count = 21

        vbox:
            style "inventory_container"
            text "Inventory" style "inventory_titel"
         
            viewport id "vp":
                # The original dynamics vscrollbar bar argument is removed here, In this version we are using the Renpy function, If you want to use the previous version you can always check the previous git version.
                ysize 475
                draggable True
                mousewheel True
                scrollbars "vertical"  
                vscrollbar_xsize 10
                vscrollbar_ysize 475
                vscrollbar_ypos 0
                vscrollbar_xpos -35
                # Below two lines of code is to add Some custom scroll bar graphics to avoid the boarding default scroll bar, for now I am going to deactivate it because I don't have any graphics yet for custom scrollbar. just Adding an option if you need that.
                # vscrollbar_base_bar "gui/qm_vscrollbar_base_bar.png"
                # vscrollbar_thumb "gui/qm_vscrollbar_thumb.png"
                vscrollbar_unscrollable "hide"
                vpgrid cols 7:
                    style "inventory_grid"
                 
    
                    
                    for slot in range(slot_count):
                        frame:
                            maximum(155, 155)
                            if slot < len(inventory.get_items()):
                                background Image("images/inventory/inventory_gui/slot_bg.png") xalign 0.5 yalign 0.5
                                add Image("images/inventory/" + inventory.get_items()[slot] + ".png", xalign=0.5, yalign=0.5)
                                $ item_name = inventory.get_items()[slot]
                                $ item_quantity = inventory.items[item_name]
                                $ Inv_item_name = item_name.replace('_', ' ')
                                $ Inv_item_quantity = f"x{item_quantity}"
                                text Inv_item_name style "inventory_item_name"
                                text Inv_item_quantity style "inventory_item_quantity"
                            else:
                                background Image("images/inventory/inventory_gui/slot_bg.png") xalign 0.5 yalign 0.5
