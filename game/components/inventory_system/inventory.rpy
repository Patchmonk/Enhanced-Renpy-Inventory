init python:
    class Inventory:
        def __init__(self, slot_count=21, unlocked_slots=7):
            self.slot_count = slot_count
            self.unlocked_slots = unlocked_slots
            self.max_items_per_slot = 99
            self.slots = [{} for _ in range(self.slot_count)]

        def add_item(self, item, quantity=1):
            if self.unlocked_slots == 0:
                show_custom_notification("No unlocked slots available.", sound_type="error")
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
                show_custom_notification(f"Could not add {remaining_quantity} {item} - no slots available.", sound_type="error")

        def remove_item(self, item, quantity=1):
            if quantity <= 0:
                show_custom_notification("Invalid quantity to remove.", sound_type="error")
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
                show_custom_notification(f"Could not fully remove {original_quantity} {item}(s) - insufficient quantity.", sound_type="error")
            else:
                show_custom_notification(f"Removed {original_quantity - quantity} {item}(s).", sound_type="remove")


        def unlock_slots(self, count):
            self.unlocked_slots = min(self.slot_count, self.unlocked_slots + count)

        def get_items(self):
            return self.slots

        def is_slot_unlocked(self, slot):
            return slot < self.unlocked_slots

        def increase_slot_count(self, additional_slots):
            self.slot_count += additional_slots
            self.slots.extend([{} for _ in range(additional_slots)])

 
