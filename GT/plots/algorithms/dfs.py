from .plotting_resources import *
from .input import *

# array that stores the edges (in object form) to be plotted
lines = []


class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def dfs(self, node, visited):
        if node not in visited:
            # print(node)
            global prev_node
            if node != prev_node:
                lines.append(
                    returnline(
                        name_to_longlat[prev_node],
                        name_to_longlat[node],
                    )
                )

            visited.add(node)
            for neighbor, _ in self.get_neighbors(node):
                prev_node = node
                self.dfs(neighbor, visited)

    def dfs_traversal(self, start_node):
        visited = set()
        # print("DFS Traversal:")
        self.dfs(start_node, visited)


prev_node = ""

def runDFS(start, prev):
    graph = Graph(adjacency_list)
    start_node = start
    global prev_node
    prev_node = prev
    graph.dfs_traversal(start_node)

    plot_all_markers()
    animate_map(lines)
    m.save("index.html")

    import webbrowser

    webbrowser.open("index.html")
