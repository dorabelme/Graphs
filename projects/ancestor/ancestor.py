# from util import Stack, Queue


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist.")


def earliest_ancestor(ancestors, starting_node):
    # Build the graph
    graph = Graph()

    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        # Build edges in reverse
    for pair in ancestors:
        graph.add_edge(pair[1], pair[0])

    # Do a BFS (storing the path)
    q = Queue()
    q.enqueue([starting_node])
    max_path_len = 1
    earliest_ancestor = -1

    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]

        # If the path is longer or equal and the value is smaller, or if the path is longer
        if (len(path) >= max_path_len and v < earliest_ancestor) or (len(path) > max_path_len):
            earliest_ancestor = v
            max_path_len = len(path)
        for neighbor in graph.vertices[v]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)
    return earliest_ancestor


# def earliest_ancestor(ancestors, starting_node):
#     queue = Queue()
#     queue.enqueue([starting_node])
#     visited_nodes = set()
#     has_parent = False
#     longest_path = []

#     while queue.size() > 0:
#         current_path = queue.dequeue()
#         if len(current_path) > len(longest_path):
#             longest_path = current_path

#         elif len(current_path) == len(longest_path):
#             if current_path[-1] < longest_path[-1]:
#                 longest_path = current_path

#         vertex = current_path[-1]

#         if vertex not in visited_nodes:
#             visited_nodes.add(vertex)
#             for i in range(0, len(ancestors)):
#                 if ancestors[i][1] is vertex:
#                     has_parent = True
#                     test_path = list(current_path)
#                     test_path.append(ancestors[i][0])
#                     queue.enqueue(test_path)

#             if has_parent is False:
#                 return - 1

#     return longest_path[-1]
