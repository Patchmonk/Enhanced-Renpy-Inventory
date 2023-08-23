screen inventoryScreen():
    modal True
    frame style style["inventory_frame"]:
        imagebutton style style["close_btn"]:
            idle "close"
            hover "close_hover"
            action Hide("inventoryScreen")

        $ slot_count = inventory.slot_count

        vbox style style["Inv_vbox"]:
            text "Inventory" style style["Inv_vbox_title"]
            vpgrid cols 7 style style["Inv_grid"]:
                if slot_count > 21:
                    draggable True mousewheel True scrollbars "vertical" style style["inv_scrollbar"]
                else:
                    draggable False mousewheel False
                 
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
                            text Inv_item_name style style["Inv_item_name"]
                            text Inv_item_quantity style style["Inv_item_quantity"]
                        else:
                            background Image("images/inventory/inventory_gui/slot_bg.png") xalign 0.5 yalign 0.5
