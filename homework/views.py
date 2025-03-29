import requests
import json
from django.shortcuts import render, get_object_or_404
from .models import Homework
from django.http import HttpResponse
from library.models import Book, Reader, Author

def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/todos/")
    if response.status_code == 200:
        return response.json()
    return []

def home(request):
    homeworks = Homework.objects.all()
    return render(request, 'homework/home.html', {'homeworks': homeworks})

def homework_detail(request, pk):
    homework = get_object_or_404(Homework, id=pk)
    json_data = None
    books = None
    reader = None
    if homework.id == 4:
        books = Book.objects.all()
        reader = Reader.objects.all()
    if homework.id == 2:
        json_data = fetch_data()

    return render(request, 'homework/detail.html', {'homework': homework, 'json_data': json_data, 'books': books, 'reader': reader})


def hello_world(request):
    return HttpResponse("<h1 style='color:green; text-align:center;'>Hello world!</h1>")
