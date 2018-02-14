class Room():
    def __init__(self, name, description, id):
        self.name = name
        self.description = description
        self.id = id
        self.items = []
        self.rooms = {}


    def add_item(self, item):
        self.items.append(item)


    def add_room(self, direction, room):
        self.rooms[direction] = room


 kitchen = Room('kitchen', 'You are in the kitchen of this trashy little house, and oh god margaret, the carpet is awful', 'k')
 dining = Room('dining', 'You are in a dining room and there is crap all over the table', 'd')
 hallway = Room('Hallway', 'You are in the hallway', 'h')
 Bedroom1 = Room('Bedroom1', 'You are in the bedroom, it smells like shizzle', 'b1)
 Bedroom2 = Room('Bedroom2', 'You are in the bedroom, it smells like shizzle', 'b2)
 Bedroom3 = Room('Bedroom3', 'You are in the bedroom, it smells like shizzle', 'b3)

 kitchen.add_room("n", 'kitchen')
 hallway.add_room("e", 'hallway')
 bedroom2.add_room("e", 'bedroom2')
 hallway.add_room("e", 'hallway')
 bedroom1.add_room("n", 'bedroom1')
