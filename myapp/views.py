from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "base.html")


def home_view(request):
    return render(request, "myapp/home.html")


def contato_view(request):
    return render(request, "myapp/contato.html")
