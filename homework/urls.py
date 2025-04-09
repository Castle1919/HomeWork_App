from django.urls import path
# from .views import home, homework_detail, hello_world, home_log, login_view
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('homework/<int:pk>/', views.homework_detail, name='homework_detail'),
    path('homework/<int:pk>/', views.go_to_homework, name='go_to_homework'),
    path('hello-world/', views.hello_world, name='hello_world'),
    path('home_log/', views.home_log, name='home_log'),
    path('login/', views.login_view, name='login'),
    path('download/', views.download_existing_zip, name='download_zip'),
    path('home_flower/', views.home_flower, name='home_flower'),
    path('about_flower/', views.about_flower, name='about_flower'),
    path('contact_flower/', views.contact_flower, name='contact_flower'),
    path('manage_data/', views.manage_data, name='manage_data')
    
]
