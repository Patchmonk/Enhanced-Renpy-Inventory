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
                vpgrid cols 7:
                    style "inventory_grid"

                    for slot in range(inventory.slot_count):
                        frame:
                            maximum(155, 155)
                            if inventory.is_slot_unlocked(slot):
                                if inventory.slots[slot]:
                                    background Image("images/inventory/inventory_gui/slot_bg.png")
                                    for item, quantity in inventory.slots[slot].items():
                                        add Image("images/inventory/" + item + ".png")
                                        $ Inv_item_name = item.replace('_', ' ')
                                        $ Inv_item_quantity = f"x{quantity}"
                                        text Inv_item_name style "inventory_item_name"
                                        text Inv_item_quantity style "inventory_item_quantity"
                                else:
                                    background Image("images/inventory/inventory_gui/slot_bg.png")
                            else:
                                background Image("images/inventory/inventory_gui/locked_slot_bg.png")
