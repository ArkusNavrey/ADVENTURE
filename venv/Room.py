-


class Room():
    +

    class Room:
        def __init__(self, name, description, id):
            self.name = name
            self.descrition = description
            self.id = id

    +        self.connectors = []
    self.items = []
    self.rooms = {}


+


def add_item(self, item):
    self.items.append(item)


def add_room(self, direction, room):
    self.rooms[direction] = room


-


def connect_rooms(self, direction, room):
    -        opposite_direction = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e', 'u': 'd', 'd': 'u'}


-        self.add_room(direction, room)
-        room.add_room(opposite_direction[direction], self)
-


def enter_room(self):
    print self.name
    print
    print self.descrition
    print


-
for direction in self.rooms.keys():
    -            print
    "to the '" + direction + "' is a " + self.rooms[direction].get_name() + '\n'
-
+
if len(self.connectors) > 0:
    +
    for connector in self.connectors:
        +                print
    "There is a " + connector[0] + "' that goes " + connector[1] + '\n'
+


def add_connection(self, room, connector, actions):
    +
    for direction in actions:
        +            self.rooms[direction] = room


+        self.connectors.append((connector, actions[0]))


def get_name(self):
    return self.name


@ @


-34, 33 + 35, 17 @ @


def is_valid_direction(self, direction):
    def next_room(self, direction):
        return self.rooms[direction]


-kitchen = Room('kitchen', "You are in the kitchen.", 1)
-dining = Room('dining room', 'you are in the dining room', 2)
-hallway = Room('hallway', 'you are in the hallway', 3)
-hallway2 = Room('upstairs hallway', "You are in the upstairs hallway", 4)
-bedroom = Room('bedroom', 'you are in the bedroom', 5)
-bedroom2 = Room('bedroom', 'You are in the bedroom', 6)
-bedroom3 = Room('bedroom', 'You are in the bedroom', 7)
-living = Room('living room', 'you are in the living room', 8)
-
-kitchen.connect_rooms('n', dining)
-dining.connect_rooms('n', hallway)
-hallway.connect_rooms('u', hallway2)
-living.connect_rooms('w', hallway)
-hallway2.connect_rooms('n', bedroom)
-hallway2.connect_rooms('e', bedroom2)
-hallway2.connect_rooms('w', bedroom3)
-
-current_room = dining
-dining.enter_room()
-
-
while True:
    -    direction = raw_input("Where shall we go eh bud?\n")
-    print
-
if direction == 'x':
    -
    break
- elif current_room.is_valid_direction(direction):
-        current_room = current_room.next_room(direction)
-        current_room.enter_room()
- else:
-        print
'Stop that \n'
+


def process_command(self, command, inventory):
    +
    if command in self.rooms.keys():
        +            new_room = self.next_room(command)


+
return new_room
+ elif "get" in command:
+
for item in self.items:
    +
    if item.name in command:
        +                    inventory.add(item)
+                    self.items.remove(item)
+
return "You picked up the " + item.name + "."
+ else:
+
return "I'm supposed to pick up something which does not exist?"
+ else:
+
return None