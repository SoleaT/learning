import datetime

from django import forms

from blog import models

from django.forms import ModelChoiceField


class MyModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "My Object #%i" % obj.id


class AuthorForm(forms.Form):
    name = forms.CharField(label='', max_length=70, widget=forms.TextInput(attrs={'class': 'input_text long_input',
                                                                                  'placeholder': 'Имя автора: ',
                                                                                  'size': '320px'}))
    surname = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'input_text long_input',
                                                                      'placeholder': 'Фамилия автора:'}), max_length=70)
    email = forms.EmailField(initial='E-mail:', label='',
                             widget=forms.EmailInput(attrs={'class': 'input_text long_input'}))
    bio = forms.CharField(initial='биография', label='',
                          widget=forms.Textarea(attrs={'class': 'input_text long_input'}))
    birthdate = forms.DateField(initial=datetime.date.today(), label='',
                                widget=forms.DateInput(attrs={'class': 'input_text long_input', 'type': 'date'}))


class ArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'author_id', 'content', 'public_date']
        labels = {'title': '', 'author_id': '', 'content': '', 'public_date': ''}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input_text long_input', 'placeholder': 'Название статьи:'}),
            'author_id': forms.Select(attrs={'class': 'input_text long_input'}),
            'content': forms.Textarea(
                attrs={'class': 'input_text long_input', 'cols': 100, 'rows': 10, 'placeholder': 'Содержание статьи'}),
            'public_date': forms.DateInput(attrs={'class': 'input_text long_input', 'type': 'date'}),
        }

