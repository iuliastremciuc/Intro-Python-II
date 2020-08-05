class Item:
    def __init__(self, item_name, item_description):
        self.item_name = item_name
        self.item_description = item_description
        self.item_list = []

    def __str__(self):
        return "{}, {}".format(self.item_name, self.item_description)

    def take_item(self):
        self.item_list.append(self.item_name)