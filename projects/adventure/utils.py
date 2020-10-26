class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def head(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


def traverse(graph):
    """
    Print each vertex in depth-first order
    beginning from starting_vertex.
    """

    # stack that contains our current path
    current_path = Stack()

    # array that contains our returned path
    moves = []

    # helps us determine if we hit a dead end
    visited = set()

    # initialize traversal with the 0 index room
    current_path.push(0)

    while len(visited) < len(graph):
        # get the id of the current room (can't pop it off since that destroys the integrity of the path)
        id = current_path.head()
        # mark as visited
        visited.add(id)
        # get the current room details (i.e. adjacent rooms)
        current_room = graph[id]
        # isolated adjacent rooms
        adjacent_rooms = current_room[1]
        # array to track if the adjacent rooms are visited or not
        undiscovered = []

        # store undiscovered rooms adjacent to current room
        for direction, adjacent_id in adjacent_rooms.items():
            if adjacent_id not in visited:
                undiscovered.append(adjacent_id)

        # assign the next room
        # if we reached a dead end, back track to a the room before it and retry in next loop
        if len(undiscovered) > 0:
            next_room = undiscovered[0]
            current_path.push(next_room)
        else:
            current_path.pop()
            next_room = current_path.head()

        # survey the adjacent rooms again. if the next_room is the adjacent room id, add that to moves
        for direction, adjacent_id in adjacent_rooms.items():
            if adjacent_id == next_room:
                moves.append(direction)
    return moves