from django.urls import path
from myapp.views import index, home_view, contato_view

urlpatterns = [
    path("", index, name="base"),
    path("home/", home_view, name="home"),
    path("contato/", contato_view, name="contato"),
]
