screen inventoryScreen():
    modal True
    frame:
        style "inventory_frame"
        imagebutton:
            style "close_btn"
            idle "close"
            hover "close_hover"
            action Hide("inventoryScreen")

        vbox:
            style "inventory_container"
            text "Inventory" style "inventory_title"
         
            viewport id "vp":
                ysize 475
                draggable True
                mousewheel True
                scrollbars "vertical"
                vscrollbar_xsize 10
                vscrollbar_ysize 475
                vscrollbar_ypos 0
                vscrollbar_xpos -35
                vscrollbar_unscrollable "hide"

                # Dynamically display inventory items
                vpgrid cols 7 :
                    style "inventory_grid"

                    # Loop through items dynamically
                    for item_name, item_quantity in inventory.items.items():
                        frame:
                            maximum(155, 155)
                            background Image("images/inventory/inventory_gui/slot_bg.png") xalign 0.5 yalign 0.5
                            add Image("images/inventory/" + item_name.split("_")[0] + ".png", xalign=0.5, yalign=0.5)

                            $ Inv_item_name = item_name.replace('_', ' ')
                            $ Inv_item_quantity = f"x{item_quantity}"

                            text Inv_item_name style "inventory_item_name"
                            text Inv_item_quantity style "inventory_item_quantity"

                    # Add empty slots to fill the grid
                    for _ in range(inventory.slot_count - len(inventory.items)):
                        frame:
                            maximum(155, 155)
                            background Image("images/inventory/inventory_gui/slot_bg.png") xalign 0.5 yalign 0.5
