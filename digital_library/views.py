from django.shortcuts import render
from .models import *
from .forms import BookForm, CategoryForm

# Create your views here.


def books(request):

    if request.method == "POST":
        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()

    return render(
        request,
        "books.html",
        {
            "books": Book.objects.all(),
            "cat": Category.objects.all(),
            "form_category": CategoryForm(),
        },
    )


def delete(request):

    if request.method == "POST":
        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()

    return render(
        request,
        "delete.html",
        {
            "form_category": CategoryForm(),
            "cat": Category.objects.all(),
        },
    )


def index(request):
    if request.method == "POST":
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()

    if request.method == "POST":
        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()

    return render(
        request,
        "index.html",
        {
            "books": Book.objects.all(),
            "cat": Category.objects.all(),
            "num": str(Book.objects.count()),
            "form": BookForm(),
            "form_category": CategoryForm(),
        },
    )


def update(request):

    if request.method == "POST":
        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()

    return render(
        request,
        "update.html",
        {
            "form_category": CategoryForm(),
            "cat": Category.objects.all(),
        },
    )
