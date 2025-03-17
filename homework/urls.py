from django.urls import path
from .views import home, homework_detail, hello_world

urlpatterns = [
    path('', home, name='home'),
    path('homework/<int:pk>/', homework_detail, name='homework_detail'),
    path('hello-world/', hello_world, name='hello_world'),

]
