from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import BookForm, CategoryForm

# Create your views here.


def books(request):

    if request.method == "POST":
        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()

    # البحث فقط في اسم الكتاب
    title_filter = request.GET.get("search_name", "")
    if title_filter:  # إذا فيه نص مكتوب
        books = Book.objects.filter(title__icontains=title_filter)
    else:  # إذا فارغ أو ممسوح
        books = Book.objects.all()

    return render(
        request,
        "books.html",
        {
            "books": books,
            "cat": Category.objects.all(),
            "form_category": CategoryForm(),
        },
    )


def delete(request, id):

    if request.method == "POST":
        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()

    book_delete = get_object_or_404(Book, id=id)
    if request.method == "POST":
        book_delete.delete()
        return redirect("/")

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

        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()

    books = Book.objects.all()

    # حساب الأرباح من البيع
    sold_total = sum(
        book.price for book in books if book.status == "sold" and book.price
    )

    # حساب الأرباح من الاستعارة
    rented_total = sum(
        (book.rental_price_day or 0) * (book.rental_period or 1)
        for book in books
        if book.status == "rented"
    )

    total_salary = sold_total + rented_total

    # حساب عدد الكتب حسب الحالة
    sold_count = books.filter(status="sold").count()
    rented_count = books.filter(status="rented").count()
    available_count = books.filter(status="available").count()

    return render(
        request,
        "index.html",
        {
            "books": books,
            "cat": Category.objects.all(),
            "num": str(Book.objects.count()),
            "form": BookForm(),
            "form_category": CategoryForm(),
            "sold_total": sold_total,
            "rented_total": rented_total,
            "total_salary": total_salary,
            "sold_count": sold_count,
            "rented_count": rented_count,
            "available_count": available_count,
        },
    )


def update(request, id):

    if request.method == "POST":
        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()

    book_id = Book.objects.get(id=id)

    if request.method == "POST":
        book_save = BookForm(request.POST, request.FILES, instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect("/")

    else:
        book_save = BookForm(instance=book_id)

    return render(
        request,
        "update.html",
        {
            "form_category": CategoryForm(),
            "cat": Category.objects.all(),
            "form": BookForm(),
            "form_book": book_save,
        },
    )
