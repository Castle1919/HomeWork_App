import requests
import json
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Homework
from django.http import FileResponse, HttpResponse
from library.models import Book, Reader, Author
import os
from django.conf import settings
from .forms import ProductForm, OrderForm, ArticleForm
from .models import Product, Order, Article

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
    zip_path = os.path.abspath(os.path.join(settings.MEDIA_ROOT, zip_filename))
    if os.path.exists(zip_path):
        return FileResponse(open(zip_path, 'rb'), as_attachment=True, filename=zip_filename)
    else:
        return HttpResponse("Файл не найден!", status=404)
    
def home_flower(request):
    return render(request, 'homework/home_flower.html')

def about_flower(request):
    return render(request, 'homework/about_flower.html')

def contact_flower(request):
    return render(request, 'homework/contact_flower.html')

def manage_data(request):
    product_form = ProductForm(request.POST or None)
    order_form = OrderForm(request.POST or None)
    article_form = ArticleForm(request.POST or None)

    if request.method == 'POST':
        if 'product_submit' in request.POST:
            if product_form.is_valid():
                product_form.save()
                return redirect('manage_data')
            else:
                print(product_form.errors)
        elif 'order_submit' in request.POST:
            if order_form.is_valid():
                order_form.save()
                return redirect('manage_data')
            else:
                print(order_form.errors) 
        elif 'article_submit' in request.POST:
            if article_form.is_valid():
                article_form.save()
                return redirect('manage_data')
            else:
                print(article_form.errors)

    products = Product.objects.all()
    orders = Order.objects.all()
    articles = Article.objects.all()

    context = {
        'product_form': product_form,
        'order_form': order_form,
        'article_form': article_form,
        'products': products,
        'orders': orders,
        'articles': articles,
    }

    return render(request, 'homework/manage_data.html', context)
