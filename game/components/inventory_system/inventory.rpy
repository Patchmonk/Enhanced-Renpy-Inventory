init python:
    class Inventory:
        def __init__(self, slot_count=21, unlocked_slots=7):
            self.slots = [{} for _ in range(slot_count)]
            self.slot_count = slot_count
            self.unlocked_slots = unlocked_slots
            self.max_items_per_slot = 99

        def add_item(self, item, quantity=1):
            remaining_quantity = quantity

            # First, try to fill existing stacks of the same item
            for slot in range(self.unlocked_slots):
                if item in self.slots[slot]:
                    space_left = self.max_items_per_slot - self.slots[slot][item]
                    if space_left > 0:
                        add_quantity = min(remaining_quantity, space_left)
                        self.slots[slot][item] += add_quantity
                        remaining_quantity -= add_quantity
                        if remaining_quantity == 0:
                            return

            # If there's still quantity to add, find empty slots
            for slot in range(self.unlocked_slots):
                if not self.slots[slot]:
                    add_quantity = min(remaining_quantity, self.max_items_per_slot)
                    self.slots[slot][item] = add_quantity
                    remaining_quantity -= add_quantity
                    if remaining_quantity == 0:
                        return

            if remaining_quantity > 0:
                print(f"Could not add {remaining_quantity} {item}(s) - no slots available.")

        def remove_item(self, item, quantity=1):
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

        def unlock_slots(self, count):
            self.unlocked_slots = min(self.slot_count, self.unlocked_slots + count)

        def get_items(self):
            items = []
            for slot in range(self.slot_count):
                items.append(self.slots[slot])
            return items

        def is_slot_unlocked(self, slot):
            return slot < self.unlocked_slots

 
