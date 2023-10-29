from collections import deque

class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def dfs(self, node, visited):
        if node not in visited:
            print(node)
            visited.add(node)
            for neighbor, _ in self.get_neighbors(node):
                self.dfs(neighbor, visited)

    def dfs_traversal(self, start_node):
        visited = set()
        print("DFS Traversal:")
        self.dfs(start_node, visited)


adjacency_list = {
    "A": [("B", 1), ("C", 3), ("D", 7)],
    "B": [("D", 5)],
    "C": [("D", 12)],
    "D": [],
}

graph = Graph(adjacency_list)
start_node = "A"
graph.dfs_traversal(start_node)
