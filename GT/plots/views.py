from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

from .algorithms.dfs import runDFS
from .algorithms.a_star import run_a_star
from .algorithms.degree_centrality import run_degree_centrality
from .algorithms.radial_dfs import run_radial_dfs

import os

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dfs(request):
    if request.method=='POST':
        form = dfs_input_form(request.POST)
        if form.is_valid():
            if os.path.exists("index.html"):
                os.remove("index.html")
            start_node = form.cleaned_data['Start']
            runDFS(start_node, start_node)

            return HttpResponse("DFS algorithm executed successfully.")

    else:
        if os.path.exists("index.html"):
            os.remove("index.html")
        form = dfs_input_form()
    
    return render(request, "dfs.html", {"form": form})

def a_star(request):
    if request.method=='POST':
        form = a_star_form(request.POST)
        if form.is_valid():
            Start = form.cleaned_data['Start']
            End = form.cleaned_data['End']

            run_a_star(Start, End)

            return HttpResponse("valid form")
    else:
        form = a_star_form()

    return render(request, "a_star.html", {"form": form})

def centrality(request):
    if(request.method=='POST'):
        form = deg_centrality_form(request.POST)
        if form.is_valid():
            Node = form.cleaned_data['Node']
            run_degree_centrality(Node)

            return HttpResponse("valid form")
    else:
        form = deg_centrality_form()
    
    return render(request, "centrality.html", {"form": form})

def radial(request):
    if(request.method=='POST'):
        form = radial_form(request.POST)
        if form.is_valid():
            Node = form.cleaned_data['Start']
            run_radial_dfs(Node)

            return HttpResponse("valid form")
    else:
        form = radial_form()
    return render(request, "radial.html", {"form": form})