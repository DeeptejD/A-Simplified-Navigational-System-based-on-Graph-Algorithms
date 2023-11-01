from collections import deque
from input import *
from main import *
from plotting_resources import *


class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def degree_centrality(self, node):
        for m, weight in self.get_neighbors(node):
            lines.append(returnline(name_to_longlat[node], name_to_longlat[m]))

        neighbors = self.get_neighbors(node)
        degree = len(neighbors)
        return degree


# Example usage
# adjacency_list = {
#     "A": [("B", 1), ("C", 3), ("D", 7)],
#     "B": [("D", 5)],
#     "C": [("D", 12)],
#     "D": [],
# }

graph = Graph(adjacency_list)
node_to_check = "mapusa"
centrality = graph.degree_centrality(node_to_check)
print(f"Degree centrality of node {node_to_check}: {centrality}")


animate_map()
m.save("index.html")

import webbrowser

webbrowser.open("index.html")
