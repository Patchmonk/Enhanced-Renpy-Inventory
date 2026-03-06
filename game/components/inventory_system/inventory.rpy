# Version 1.6 – Inventory Consistency Update

# Reason:
# This describes exactly what happened without exposing technical jargon like “case normalization”. 
# It’s clear and straightforward for players to understand that the system will now treat “Potion” and “potion” as the same item, 
# which is a common expectation in inventory systems. The term “case normalization” might be confusing for non-technical players, 
# while the new description directly communicates the change in behavior.

# ==================================
# == 🎒 Inventory System Setup ==
# ==================================
# 💡 Here we create the actual inventory! It's like giving the player a backpack.
# Initializing the inventory system in Ren'Py. The most common approach is to initialize this variable within the Script RPY file.
# There are two parameters in the default inventory variable: `slot_count=21` (total slots) and `unlocked_slots=7` (initial unlocked slots).  
default inventory = Inventory(slot_count=21, unlocked_slots=7) # we just introduce the Inventory system to Renpy.


# ================================ 
# 💼 Inventory system custom code 
# ================================ 

init python:
    class Inventory:

        def __init__(self, slot_count=21, unlocked_slots=7):
            self.slot_count = slot_count
            self.unlocked_slots = unlocked_slots
            self.max_items_per_slot = 99
            self.slots = [{} for _ in range(self.slot_count)]

        # ==================================
        # Normalize item keys (Case Fix)
        # ==================================
        def _normalize_item(self, item):
            return str(item).strip().lower()


        def add_item(self, item, quantity=1):

            item = self._normalize_item(item)

            if self.unlocked_slots == 0:
                pm_notify("No unlocked slots available.", sound_type="error")
                return

            if quantity <= 0:
                return

            remaining_quantity = quantity
            
            # First, try to add to existing slots with the same item
            for slot in range(self.unlocked_slots):
                if item in self.slots[slot]:
                    space_left = self.max_items_per_slot - self.slots[slot][item]

                    if space_left > 0:
                        add_quantity = min(remaining_quantity, space_left)
                        self.slots[slot][item] += add_quantity
                        remaining_quantity -= add_quantity

                        if remaining_quantity == 0:
                            return

            # Next, try to add to empty slots
            for slot in range(self.unlocked_slots):
                if not self.slots[slot]:
                    add_quantity = min(remaining_quantity, self.max_items_per_slot)

                    self.slots[slot][item] = add_quantity
                    remaining_quantity -= add_quantity

                    if remaining_quantity == 0:
                        return
            
            # If there are still remaining items, show a notification
            if remaining_quantity > 0:
                pm_notify(f"Could not add {remaining_quantity} {item} - no slots available.", sound_type="error")


        def remove_item(self, item, quantity=1):
            item = self._normalize_item(item)

            if quantity <= 0:
                pm_notify("Invalid quantity to remove.", sound_type="error")
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

            if quantity > 0:
                pm_notify(f"Could not fully remove {original_quantity} {item} - insufficient quantity.", sound_type="error")
                self.sort_inventory()  # Call sort_inventory after removal
            else:
                pm_notify(f"{original_quantity - quantity} {item} Removed.", sound_type="remove")
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
            pm_notify(f"Slot count increased by {additional_slots}!", sound_type="success")


        def unlock_slots(self, count):
            self.unlocked_slots = min(self.slot_count, self.unlocked_slots + count)
            pm_notify(f"Unlocked {count} new slots.", sound_type="success")


        def is_slot_unlocked(self, slot):
            return slot < self.unlocked_slots


        def lock_slots(self, count):
            if count <= self.unlocked_slots:
                self.unlocked_slots -= count
                # pm_notify(f"Locked {count} slots.", sound_type="error")
                pm_notify(" Warning: slots are locked!", sound_type="error")
            else:
                pm_notify("Not enough unlocked slots to lock.", sound_type="error")


        def get_items(self):
            return self.slots
        
        def has_item(self, item, quantity=1):
            item = self._normalize_item(item)
            total = 0
            for slot in self.slots:
                if item in slot:
                    total += slot[item]
            return total >= quantity  # Returns True if inventory has at least 'quantity' of item