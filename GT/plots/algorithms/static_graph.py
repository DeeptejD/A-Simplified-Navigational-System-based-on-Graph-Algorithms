from plotting_resources import *
from input import *

# array that stores the edges (in object form) to be plotted
lines = []

for edge in edges:
    lines.append([[edge[0][1], edge[0][0]], [edge[1][1], edge[1][0]]])

plot_all_markers()
plot_static_map(lines)

# Save the map to an HTML file
m.save("index.html")
import webbrowser

webbrowser.open("index.html")
