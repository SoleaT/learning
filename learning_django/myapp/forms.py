from re import sub
from django import forms
from django.core.exceptions import ValidationError
from myapp import models


def validate_phone(value):
    phone = sub(r'[\s +.()\-]', '', value)
    if not phone.isdigit():
        raise ValidationError(u'Можно использовать только цифры.')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = '__all__'
        widgets = {'cat_name': forms.TextInput(
            attrs={'class': 'input_text long_input', 'placeholder': 'Название категории: '})}
        labels = {'cat_name': ''}


class ClientForm(forms.ModelForm):
    phone = forms.CharField(validators=[validate_phone], initial='89999999999')

    class Meta:
        model = models.Client
        fields = ['name', 'email', 'address']
        labels = {i: '' for i in fields}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input_text long_input', 'placeholder': 'Имя: '}),
            'email': forms.EmailInput(attrs={'class': 'input_text', 'placeholder': 'E-mail: '}),
            'address': forms.TextInput(attrs={'class': 'input_text long_input', 'placeholder': 'Адрес: '}),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['p_name', 'p_description', 'price', 'category', 'quantity', 'image_link']
        labels = {i: '' for i in fields}
        widgets = {
            'p_name': forms.TextInput(attrs={'class': 'input_text long_input', 'placeholder': 'Название товара'}),
            'p_description': forms.Textarea(attrs={'class': 'input_text long_input', 'placeholder': 'Описание товара'}),
            'price': forms.NumberInput(attrs={'class': 'input_text long_input', 'placeholder': 'Цена'}),
            'image_link': forms.FileInput(attrs={'class': 'input_text long_input'}),
            'quantity': forms.NumberInput(attrs={'class': 'input_text long_input'}),
            'category': forms.Select(attrs={'class': 'input_text long_input'})
        }
