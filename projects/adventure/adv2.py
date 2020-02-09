from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


def run_code():
    # Load world
    world = World()

    # You may uncomment the smaller graphs for development and testing purposes.
    map_file = "maps/test_line.txt"
    map_file = "maps/test_cross.txt"
    map_file = "maps/test_loop.txt"
    map_file = "maps/test_loop_fork.txt"
    map_file = "maps/main_maze.txt"

    # Loads the map into a dictionary
    room_graph = literal_eval(open(map_file, "r").read())
    world.load_graph(room_graph)

    # Print an ASCII map
    world.print_rooms()

    player = Player(world.starting_room)

    # Fill this out with directions to walk
    # traversal_path = ['n', 'n']
    mygraph = {}
    traversal_path = []

    def opposite(direction):
        if direction == 'n':
            return 's'
        elif direction == 's':
            return 'n'
        elif direction == 'e':
            return 'w'
        elif direction == 'w':
            return 'e'

    def bfs_path(graph, start_room):
        queue = []
        queue.append([start_room])
        visit = set()

        while queue:
            path = queue.pop(0)
            x_room = path[-1]
            if x_room not in visit:
                visit.add(x_room)
                for room_exit in graph[x_room]:
                    if graph[x_room][room_exit] == '?':
                        return path
                for x in graph[x_room]:
                    adjacent_room = graph[x_room][x]
                    new_path = list(path)
                    new_path.append(adjacent_room)
                    queue.append(new_path)
        return None

    while len(mygraph) != len(room_graph):
        current = player.current_room.id
        if current not in mygraph:
            mygraph[current] = {
                i: '?' for i in player.current_room.get_exits()}

        room_exit = None
        for direction in mygraph[current]:
            if mygraph[current][direction] == '?':
                room_exit = direction
                if room_exit is not None:
                    traversal_path.append(room_exit)
                    player.travel(room_exit)
                    discovered = player.current_room.id

                    if discovered not in mygraph:
                        mygraph[discovered] = {
                            i: '?' for i in player.current_room.get_exits()}

                mygraph[current][room_exit] = discovered
                # the value of current
                mygraph[discovered][opposite(room_exit)] = current
                current = discovered  # current is now the value of discovered
                break

        # if there are no unexplored question marks
        keys = bfs_path(mygraph, player.current_room.id)
        print(keys)
        if keys is not None:
            for room in keys:
                for direction in mygraph[current]:
                    print(f"mg d", mygraph[current])
                    if mygraph[current][direction] == room:
                        traversal_path.append(direction)
                        player.travel(direction)
                current = player.current_room.id

    print(mygraph)

    # TRAVERSAL TEST
    visited_rooms = set()
    player.current_room = world.starting_room
    visited_rooms.add(player.current_room)

    for move in traversal_path:
        player.travel(move)
        visited_rooms.add(player.current_room)

    if len(visited_rooms) == len(room_graph):
        print(
            f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
    else:
        print("TESTS FAILED: INCOMPLETE TRAVERSAL")
        print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

    return len(traversal_path)

#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")


run_code()

# min_so_far = 1200

# while True:
#     l = run_code()
#     if l <= 960:
#         break

#     min_so_far = min(min_so_far, l)
#     print(min_so_far)
