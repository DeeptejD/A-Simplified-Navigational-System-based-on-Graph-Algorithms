from .plotting_resources import *
from .input import *


class Graph:
    def __init__(self, adjacency_list):
        self.start_node = ""
        self.prev_node = ""
        self.radius = 0
        self.lines = []
        self.your_unix_timestamp = 1609459200
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def dfs(self, node, visited):
        if node not in visited:
            # print(node)
            # global prev_node
            if node != self.prev_node:
                self.lines.append(
                    returnline(
                        name_to_longlat[self.prev_node],
                        name_to_longlat[node],
                        self.your_unix_timestamp,
                    )
                )
                self.your_unix_timestamp += 450

            visited.add(node)
            for neighbor, _ in self.get_neighbors(node):
                self.prev_node = node
                if (
                    haversine(
                        name_to_longlat[self.start_node], name_to_longlat[neighbor]
                    )
                    <= self.radius
                ):
                    self.dfs(neighbor, visited)

    def dfs_traversal(self, start_node):
        visited = set()
        # print("DFS Traversal:")
        self.dfs(start_node, visited)


def run_radial_dfs(start):
    graph = Graph(adjacency_list)

    radius = 30
    graph.radius = 30

    start_node = start
    graph.start_node = start

    graph.prev_node = start_node

    # plotting requirements
    m = folium.Map([15.4986, 73.8284], zoom_start=10)

    graph.dfs_traversal(start_node)

    plot_all_markers(m)
    animate_map(graph.lines, m)
    longlat = name_to_longlat[start_node]
    radial_plotting((longlat[1], longlat[0]), radius, m)

    m.save("index.html")
    # import webbrowser

    # webbrowser.open("index.html")
