from .plotting_resources import *
from .input import *


class Graph:
    def __init__(self, adjacency_list):
        self.lines = []
        self.your_unix_timestamp = 1609459200
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def degree_centrality(self, node):
        for m, weight in self.get_neighbors(node):
            self.lines.append(
                returnline(
                    name_to_longlat[node], name_to_longlat[m], self.your_unix_timestamp
                )
            )
            self.your_unix_timestamp += 450

        neighbors = self.get_neighbors(node)
        degree = len(neighbors)
        return degree


def run_degree_centrality(node):
    graph = Graph(adjacency_list)
    node_to_check = node

    # plotting requirements
    m = folium.Map([15.4986, 73.8284], zoom_start=10)

    centrality = graph.degree_centrality(node_to_check)
    print(f"Degree centrality of node {node_to_check}: {centrality}")

    animate_map(graph.lines, m)
    plot_all_markers(m)
    m.save("index.html")

    # import webbrowser

    # webbrowser.open("index.html")
