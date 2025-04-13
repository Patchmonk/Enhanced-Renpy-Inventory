###################################################################################################################
# ██████╗  █████╗ ████████╗ ██████╗██╗  ██╗███╗   ███╗ ██████╗ ███╗   ██╗██╗  ██╗                                 #
# ██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║  ██║████╗ ████║██╔═══██╗████╗  ██║██║ ██╔╝                                 #
# ██████╔╝███████║   ██║   ██║     ███████║██╔████╔██║██║   ██║██╔██╗ ██║█████╔╝                                  #
# ██╔═══╝ ██╔══██║   ██║   ██║     ██╔══██║██║╚██╔╝██║██║   ██║██║╚██╗██║██╔═██╗                                  #
# ██║     ██║  ██║   ██║   ╚██████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝██║ ╚████║██║  ██╗                                 #
# ╚═╝     ╚═╝  ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝                                 #
###################################################################################################################
###################################################################################################################
## The Inventory class is a robust solution for managing items in a Ren'Py game. It provides essential features   #
## such as adding and removing items, dynamic slot management, and user notifications.                            #
## By implementing this class, developers can create a more engaging and interactive experience for players,      #
## allowing them to manage their inventory effectively.                                                           #
## Whether you're building a simple game or a complex RPG, this inventory system may very well be the next best   #
## thing after the RenPy included tutorials.  A valuable addition to your project saving you a lot of time.       #
## Brought to you by Patchmonk                                                                                    #
###################################################################################################################


init python:
    class Inventory:
        def __init__(self, slot_count=21, unlocked_slots=7):
            self.slot_count = slot_count
            self.unlocked_slots = unlocked_slots
            self.max_items_per_slot = 99
            self.additional_slots = 10
            self.slots = [{} for _ in range(self.slot_count)]

        def add_item(self, item, quantity=1):
            if self.unlocked_slots == 0:
                show_notification("No unlocked slots available.", sound_type="error")
                return

            remaining_quantity = quantity

            # Try to add to existing slots with the same item
            for slot in range(self.unlocked_slots):
                if item in self.slots[slot]:
                    space_left = self.max_items_per_slot - self.slots[slot][item]
                    if space_left > 0:
                        add_quantity = min(remaining_quantity, space_left)
                        self.slots[slot][item] += add_quantity
                        remaining_quantity -= add_quantity
                        if remaining_quantity == 0:
                            return

            # Try to add to empty slots
            for slot in range(self.unlocked_slots):
                if not self.slots[slot]:
                    add_quantity = min(remaining_quantity, self.max_items_per_slot)
                    self.slots[slot][item] = add_quantity
                    remaining_quantity -= add_quantity
                    if remaining_quantity == 0:
                        return

            # Notify if there are remaining items
            if remaining_quantity > 0:
                show_notification(f"Could not add {remaining_quantity} {item} - no slots available.", sound_type="error")

        def remove_item(self, item, quantity=1):
            if quantity <= 0:
                show_notification("Invalid quantity to remove.", sound_type="error")
                return

            original_quantity = quantity

            for slot in range(self.slot_count):
                if item in self.slots[slot]:
                    if quantity >= self.slots[slot][item]:
                        quantity -= self.slots[slot][item]
                        del self.slots[slot][item]
                    else:
                        self.slots[slot][item] -= quantity
                        quantity = 0
                    if quantity <= 0:
                        break
            """ modified by Bokskabouter: now it uses one sort instead of two """
            if quantity > 0:
                show_notification(f"Could not fully remove {original_quantity} {item} - insufficient quantity.", sound_type="error")
            else:
                show_notification(f"{original_quantity - quantity} {item} Removed.", sound_type="remove")
            self.sort_inventory()  # Call sort_inventory after removal

        def sort_inventory(self):
            sorted_slots = [{} for _ in range(self.slot_count)]
            current_slot = 0

            for slot in range(self.slot_count):
                if self.slots[slot]:
                    sorted_slots[current_slot] = self.slots[slot]
                    current_slot += 1

            self.slots = sorted_slots

        def increase_slot_count(self, additional_slots):
            self.slot_count += additional_slots
            self.slots.extend([{} for _ in range(additional_slots)])
            show_notification(f"Slot count increased by {additional_slots}!", sound_type="success")

        def unlock_slots(self, count):
            self.unlocked_slots = min(self.slot_count, self.unlocked_slots + count)
            show_notification(f"Unlocked {count} new slots.", sound_type="success")

        def is_slot_unlocked(self, slot):
            return slot < self.unlocked_slots

        def lock_slots(self, count):
            if count <= self.unlocked_slots:
                self.unlocked_slots -= count
                show_notification(f"Warning: {count} slots are locked!", sound_type="locked") # modified by Bokskabouter added locked sound
            else:
                show_notification("Not enough unlocked slots to lock.", sound_type="error")

        def get_items(self):
            return self.slots


        
