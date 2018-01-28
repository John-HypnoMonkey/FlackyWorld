import gameitem


class inventory():
    items = []

    @classmethod
    def add_item(cls, item):
        add_new_item = True
        for val in inventory.items:
            if item.name == val.name and not isinstance(item, gameitem.weapon):
                val.count += 1
                del item
                add_new_item = False
                break
        if add_new_item is True:
            inventory.items.append(item)
