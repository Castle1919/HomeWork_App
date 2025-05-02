from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from django.utils.text import slugify
from django.urls import reverse
from django.core.exceptions import ValidationError
import datetime
from django.utils.timezone import now


class Homework(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    json_data = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    
class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    stock = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)
        
class Order(models.Model):
    STATUS_CHOICES = [
        ('Новый', 'Новый'),
        ('В обработке', 'В обработке'),
        ('Доставлен', 'Доставлен'),
        ('Отменен', 'Отменен'),
    ]
    
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Новый')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Заказ №{self.id} - {self.status}"
    
class Article(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(default=timezone.now)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    
class Person(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name}, {self.age} лет"

class Child(Person):
    favorite_ice_cream = models.ForeignKey('IceCream', on_delete=models.SET_NULL, null=True, blank=True)

class IceCream(models.Model):
    name = models.CharField(max_length=255)
    flavor = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.flavor})"

class IceCreamKiosk(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    ice_creams = models.JSONField(default=list, blank=True)

    def __str__(self):
        return f"{self.name} ({self.location})"
    
    def get_ice_cream_list(self):
        return ", ".join([ice_cream.name for ice_cream in self.ice_creams.all()])
    
    
    
def validate_phone(value):
    if not value.startswith("+7") or len(value) != 12:
        raise ValidationError("Номер телефона должен начинаться с +7 и состоять из 12 символов.")

def validate_positive(value):
    if value < 0:
        raise ValidationError("Только положительные числа или 0.")
    
class Article_2(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    published_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})

    def is_published_recently(self):
        return self.published_at >= now() - datetime.timedelta(days=7)

    def get_id_and_title(self):
        return f"{self.id} - {self.title}"

    def __str__(self):
        return self.title

class Profile(models.Model):
    phone = models.CharField(max_length=12, validators=[validate_phone])

    def __str__(self):
        return self.phone

class SomeModel(models.Model):
    number = models.IntegerField(validators=[validate_positive])