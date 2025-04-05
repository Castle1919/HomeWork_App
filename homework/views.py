import requests
import json
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Homework
from django.http import FileResponse, HttpResponse
from library.models import Book, Reader, Author
import os
from django.conf import settings

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

    return render(request, 'homework/detail.html', {'homework': homework, 'json_data': json_data, 'books': books, 'reader': reader,})

def go_to_homework(request, pk):
    url = reverse('homework_detail', kwargs={'pk': pk})
    return redirect(url)

def hello_world(request):
    return HttpResponse("<h1 style='color:green; text-align:center;'>Hello world!</h1>")

def home_log(request):
    return render(request, 'homework/home_log.html')

def login_view(request):
    return render(request, 'homework/login.html')

def download_existing_zip(request):
    zip_filename = "scripts.zip" 
    zip_path = os.path.join(settings.MEDIA_ROOT, zip_filename)

    if os.path.exists(zip_path):
        return FileResponse(open(zip_path, 'rb'), as_attachment=True, filename=zip_filename)
    else:
        return HttpResponse("Файл не найден", status=404)
    
def home_flower(request):
    return render(request, 'homework/home_flower.html')

def about_flower(request):
    return render(request, 'homework/about_flower.html')

def contact_flower(request):
    return render(request, 'homework/contact_flower.html')
