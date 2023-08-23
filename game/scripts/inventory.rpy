init python:
    class Inventory:
        def __init__(self, slot_count=21):
            self.items = {}
            self.slot_count = slot_count
            self.max_items_per_slot = 99

        def add_item(self, item, quantity=1):
            if item in self.items:
                self.items[item] += quantity
            else:
                self.items[item] = quantity

            if self.items[item] > self.max_items_per_slot:
                self.items[item] = self.max_items_per_slot
                print("You cannot add more than {} items to this slot.".format(self.max_items_per_slot))


        def remove_item(self, item, quantity=1):
            if item in self.items:
                if quantity >= self.items[item]:
                    del self.items[item]
                else:
                    self.items[item] -= quantity

        def get_items(self):
            return list(self.items.keys())
      
      