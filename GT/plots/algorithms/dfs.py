from .plotting_resources import *
from .input import *


class Graph:
    def __init__(self, adjacency_list):
        self.path = []
        self.lines = []
        self.your_unix_timestamp = 1609459200
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def dfs(self, node, visited, prev_node):
        if node not in visited:
            # print(node)
            self.path.append(node)
            if node != prev_node:
                self.lines.append(
                    returnline(
                        name_to_longlat[prev_node],
                        name_to_longlat[node],
                        self.your_unix_timestamp,
                    )
                )
                # beacuse the updated value wont reflect
                self.your_unix_timestamp += 450

            visited.add(node)
            for neighbor, _ in self.get_neighbors(node):
                prev_node = node
                self.dfs(neighbor, visited, prev_node)

    def dfs_traversal(self, start_node, prev_node):
        visited = set()
        self.dfs(start_node, visited, prev_node)


# returns a list with the dfs (its not a path, its dfs)
def runDFS(start, prev):
    graph = Graph(adjacency_list)
    start_node = start
    prev_node = prev

    # plotting requirements
    m = folium.Map([15.4986, 73.8284], zoom_start=10)

    graph.dfs_traversal(start_node, prev_node)
    v = graph.path

    plot_all_markers(m)
    animate_map(graph.lines, m)
    m.save("index.html")

    return v
