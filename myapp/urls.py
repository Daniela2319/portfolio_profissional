from django.urls import path
from myapp.views import index, home_view, contato_view, sobre_view, projeto_view

urlpatterns = [
    path("home/", home_view, name="home"),
    path("", index, name="base"),
    path("sobre/", sobre_view, name="sobre"),
    path("projeto/", projeto_view, name="projeto"),
    path("contato/", contato_view, name="contato"),
]
