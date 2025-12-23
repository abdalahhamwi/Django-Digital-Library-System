from django.shortcuts import render
from .models import *

# Create your views here.


def books(request):
    return render(request, "books.html")


def delete(request):
    return render(request, "delete.html")


def index(request):
    return render(request, "index.html", {
        "x": Book.objects.all(),
        "num": str(Book.objects.count())
    })



def update(request):
    return render(request, "update.html")
