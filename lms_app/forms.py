from django import forms
from .models import Book, Category


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        #fiels= '__all__'
        fields = [
            'title',
            'author',
            'photo_image',
            'photo_author',
            'pages',
            'price',
            'rental_price_day',
            'rental_time',
            'total_rental',
            'status',
            'category',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'photo_image': forms.FileInput(attrs={'class': 'form-control'}),
            'photo_author': forms.FileInput(attrs={'class': 'form-control'}),
            'pages': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'rental_price_day': forms.NumberInput(attrs={'class': 'form-control','id':'rental_price'}),
            'rental_time': forms.NumberInput(attrs={'class': 'form-control','id':'rental_time'}),
            'total_rental': forms.NumberInput(attrs={'class': 'form-control','id':'total_rental','readonly':'True'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
        


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        #fiels= '__all__'
        fields = [
            'name',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}), 
        }
        labels = {
            'name': ''
        }