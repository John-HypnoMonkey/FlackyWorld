class inventory():
    items = []
    @classmethod
    def add_item(cls, item):
        add_new_item =True
        for val in inventory.items:
            if item.name == val.name:
                val.count+=1
                del item
                add_new_item = False
                break
        if add_new_item == True:
            inventory.items.append(item)

