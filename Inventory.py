class Inventory:
    def __init__(self):
        self.slots = []

    def add_item(self, item):
        self.slots.append(item)

    def __len__(self):
        return len(self.slots)

    def __contains__(self, item):
        return item in self.slots

    def __iter__(self):
        yield from self.slots


class SortedInventory(Inventory):

    def add_item(self, item):
        super().add_item(item)  # Includes Inventory class method of same name
        return self.slots.sort()
