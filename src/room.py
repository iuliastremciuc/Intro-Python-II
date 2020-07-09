# Implement a class to hold room information. This should have name and
# description attributes.
class Room():
    # n_to = n
    # s_to = s
    # e_to = e
    # w_to = w
    def __init__(self, room_name, description):
        self.room_name = room_name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def __str__(self):
        return "{}, {}".format(self.room_name, self.description)

