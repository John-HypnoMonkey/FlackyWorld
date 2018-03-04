import gameitem


class Inventory():
    items = []

    @classmethod
    def addItem(cls, item):
        add_new_item = True
        for val in Inventory.items:
            if item.name == val.name and not isinstance(item, gameitem.Weapon):
                val.count += 1
                del item
                add_new_item = False
                break
        if add_new_item is True:
            Inventory.items.append(item)
