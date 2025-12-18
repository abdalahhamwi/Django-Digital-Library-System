from django.shortcuts import render

# Create your views here.


def books(request):
    return render(request, "books.html")


def delete(request):
    return render(request, "delete.html")


def index(request):
    return render(request, "index.html")


def update(request):
    return render(request, "update.html")
