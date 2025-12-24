from django.shortcuts import render
from .models import *

# Create your views here.


def books(request):
    return render(
        request,
        "books.html",
        {
            "books": Book.objects.all(),
            "cat": Category.objects.all(),
        },
    )


def delete(request):
    return render(request, "delete.html")


def index(request):
    return render(
        request,
        "index.html",
        {
            "books": Book.objects.all(),
            "cat": Category.objects.all(),
            "num": str(Book.objects.count()),
        },
    )


def update(request):
    return render(request, "update.html")
