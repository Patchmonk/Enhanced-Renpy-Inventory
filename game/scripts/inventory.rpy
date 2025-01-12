init python:
    class Inventory:
        def __init__(self, slot_count=3):
            self.items = {}  # Dictionary to store items and their quantities in slots
            self.slot_count = slot_count
            self.max_items_per_slot = 99

        def add_item(self, item, quantity=1):
            # Find existing slots for the item or add a new one
            slots = [key for key in self.items.keys() if key.startswith(item)]
            
            # Add to existing slots if possible
            for slot in slots:
                available_space = self.max_items_per_slot - self.items[slot]
                if available_space > 0:
                    added_quantity = min(quantity, available_space)
                    self.items[slot] += added_quantity
                    quantity -= added_quantity
                    if quantity <= 0:
                        return

            # Use new slots for excess items
            while quantity > 0:
                new_slot_name = f"{item}_{len(slots) + 1}"
                if len(self.items) < self.slot_count:
                    added_quantity = min(quantity, self.max_items_per_slot)
                    self.items[new_slot_name] = added_quantity
                    quantity -= added_quantity
                    slots.append(new_slot_name)
                else:
                    print("Inventory is full! Unable to add more items.")
                    return

        def remove_item(self, item, quantity=1):
            # Find slots with the item and remove from them
            slots = sorted([key for key in self.items.keys() if key.startswith(item)])
            for slot in slots:
                if quantity <= self.items[slot]:
                    self.items[slot] -= quantity
                    if self.items[slot] == 0:
                        del self.items[slot]
                    return
                else:
                    quantity -= self.items[slot]
                    del self.items[slot]

        def get_items(self):
            return self.items

 
