from .plotting_resources import *
from .input import *

# array that stores the edges (in object form) to be plotted
lines = []


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


def run_degree_centrality(node):
    graph = Graph(adjacency_list)
    node_to_check = node
    centrality = graph.degree_centrality(node_to_check)
    print(f"Degree centrality of node {node_to_check}: {centrality}")


    animate_map(lines)
    plot_all_markers()
    m.save("index.html")

    import webbrowser

    webbrowser.open("index.html")
