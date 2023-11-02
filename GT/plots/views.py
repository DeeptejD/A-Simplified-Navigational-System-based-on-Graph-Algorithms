from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

from .algorithms.dfs import Graph, adjacency_list, animate_map,m

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dfs(request):
    if request.method=='POST':
        form = dfs_input_form(request.POST)
        if form.is_valid():
            start_node = form.cleaned_data['Start']
            graph = Graph(adjacency_list)
            # prev_node = start_node  # Initialize prev_node with the start_node
            graph.dfs_traversal(start_node)
            animate_map()
            m.save("index.html")

            import webbrowser
            webbrowser.open("index.html")

            return HttpResponse("DFS algorithm executed successfully.")

    else:
        form = dfs_input_form()
    
    return render(request, "dfs.html", {"form": form})

def a_star(request):
    if request.method=='POST':
        form = a_star_form(request.POST)
        if form.is_valid():
            return HttpResponse("valid form")
    else:
        form = a_star_form()

    return render(request, "a_star.html", {"form": form})

def centrality(request):
    if(request.method=='POST'):
        form = deg_centrality_form(request.POST)
        if form.is_valid():
            return HttpResponse("valid form")
    else:
        form = deg_centrality_form()
    
    return render(request, "centrality.html", {"form": form})