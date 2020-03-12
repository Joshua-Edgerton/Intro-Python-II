# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

#Experimental item code \/

        self.items = []

    def set_items(self, items):
        for item in items:
            self.items.append(item)
        
#Experimental item code /\

    def __str__(self):

#Experimental item code \/
        if len(self.items) >= 1:
                item_list = "\n\u001b[33mItems in room:\u001b[37m\n"

                for item in self.items:
                    item_list += "\n\n \u001b[36m¸,ø¤º°`°º¤ø,¸\u001b[34m " +item.name + " - " + item.description + " \u001b[36m¸,ø¤º°`°º¤ø,¸ \u001b[37m\n"

                return f"\u001b[35m{self.name}\n\u001b[36m{self.description}\u001b[37m \n{item_list}\n"
#Experimental item code /\

        else:
            return (f"\u001b[35m{self.name}\n\u001b[36m{self.description}\u001b[37m \n")