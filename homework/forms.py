from django import forms
from .models import Product, Order, Article, Article_2, Profile, SomeModel

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'customer_email', 'status', 'total_price']

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

class ArticleForm2(forms.ModelForm):
    class Meta:
        model = Article_2
        fields = ['title', 'content', 'slug']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone']
        def clean_phone(self):
            phone = self.cleaned_data['phone']
            if not phone.startswith("+7") or len(phone) != 12:
                raise forms.ValidationError("Ошибка: номер должен начинаться с +7 и состоять из 12 символов!")
            return phone

class SomeModelForm(forms.ModelForm):
    class Meta:
        model = SomeModel
        fields = ['number']
        def clean_number(self):
            number = self.cleaned_data['number']
            if number < 0:
                raise forms.ValidationError("Ошибка: допускаются только положительные числа и 0!")
            return number

"""
SELECT authors.name, books.title
FROM authors
INNER JOIN books ON authors.id = books.author_id;
"""