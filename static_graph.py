from .plotting_resources import *
from .input import *


def plot_static():
    # plotting requirements
    m = folium.Map([15.4986, 73.8284], zoom_start=10)
    lines = []

    for edge in edges:
        lines.append([[edge[0][1], edge[0][0]], [edge[1][1], edge[1][0]]])

    plot_all_markers(m)
    plot_static_map(lines, m)
    m.save("index.html")
    # import webbrowser

    # webbrowser.open("index.html")
