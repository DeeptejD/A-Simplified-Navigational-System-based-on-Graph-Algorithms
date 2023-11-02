from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dfs/", views.dfs, name="dfs"),
    path("a_star/", views.a_star, name="a_star"),
    path("centrality/", views.centrality, name="centrality"),
]