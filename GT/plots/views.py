from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

from .algorithms.dfs import runDFS
from .algorithms.a_star import run_a_star
from .algorithms.degree_centrality import run_degree_centrality
from .algorithms.radial_dfs import run_radial_dfs
from .algorithms.static_graph import plot_static

import os

# Create your views here.
def index(request):
    plot_static()

    with open("static_graph.html", "r") as html_file:
            html_content = html_file.read()

    return render(request, 'index.html', {'html_content': html_content})

def dfs(request):
    if request.method=='POST':
        form = dfs_input_form(request.POST)
        if form.is_valid():
            start_node = form.cleaned_data['Start']
            v= runDFS(start_node, start_node)

            # this part is used to render the index.html file in the def_template
            with open("index.html", "r") as html_file:
                html_content = html_file.read()

            return render(request, 'render_dfs_template.html', {'html_content': html_content, 'dfs_result': v})
    else:
        form = dfs_input_form()
        
        plot_static()
        with open("static_graph.html", "r") as html_file:
            html_content = html_file.read()
        
        return render(request, "dfs.html", {"form": form, 'html_content': html_content})

def a_star(request):
    if request.method=='POST':
        form = a_star_form(request.POST)
        if form.is_valid():
            Start = form.cleaned_data['Start']
            End = form.cleaned_data['End']

            v = run_a_star(Start, End)

            # this part is used to render the index.html file in the def_template
            with open("index.html", "r") as html_file:
                html_content = html_file.read()

            context = {'html_content': html_content, 'a_star_result': v}

            return render(request, 'render_astar_template.html', context)
    else:
        plot_static()
        
        with open("static_graph.html", "r") as html_file:
            html_content = html_file.read()
        
        form = a_star_form()

    return render(request, "a_star.html", {"form": form, 'html_content': html_content})

def centrality(request):
    if(request.method=='POST'):
        form = deg_centrality_form(request.POST)
        if form.is_valid():
            Node = form.cleaned_data['Node']
            centrality = run_degree_centrality(Node)

            # this part is used to render the index.html file in the def_template
            with open("index.html", "r") as html_file:
                html_content = html_file.read()

            context = {'html_content': html_content, 'centrality': centrality, 'Node':Node}

            return render(request, 'render_centrality.html', context)
    else:
        plot_static()
        with open("static_graph.html", "r") as html_file:
            html_content = html_file.read()
        form = deg_centrality_form()
    
    return render(request, "centrality.html", {"form": form, 'html_content': html_content})

def radial(request):
    if(request.method=='POST'):
        form = radial_form(request.POST)
        if form.is_valid():
            Node = form.cleaned_data['Start']
            radius_in_km = float(form.data['radius_in_km'])
            v=run_radial_dfs(Node, radius_in_km)

            # this part is used to render the index.html file in the def_template
            with open("index.html", "r") as html_file:
                html_content = html_file.read()
            
            context={'html_content': html_content, 'dfs_result':v}

            return render(request, 'render_dfs_template.html', context)
    else:
        plot_static()
        with open("static_graph.html", "r") as html_file:
            html_content = html_file.read()
        form = radial_form()
    return render(request, "radial.html", {"form": form, 'html_content': html_content})