from collections import deque

class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def degree_centrality(self, node):
        neighbors = self.get_neighbors(node)
        degree = len(neighbors)
        return degree


# Example usage
adjacency_list = {
    "A": [("B", 1), ("C", 3), ("D", 7)],
    "B": [("D", 5)],
    "C": [("D", 12)],
    "D": [],
}

graph = Graph(adjacency_list)
node_to_check = "D"
centrality = graph.degree_centrality(node_to_check)
print(f"Degree centrality of node {node_to_check}: {centrality}")
