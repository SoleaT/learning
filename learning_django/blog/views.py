import random

from django.contrib import messages
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.utils import timezone
from blog.models import Author, Article
from blog.forms import AuthorForm, ArticleForm
from faker import Faker

fake = Faker('ru-RU')


def seminar2(request):
    context = {'link_all_authors': 'list_authors',
               'link_all_articles': 'link_all_articles',
               'link_create_author': 'create_author',
               'link_create_author_r': 'create_author_random',
               'link_create_article': 'create_article',
               'link_create_articles_r': 'create_articles_r',
               'name': 'Юзер'}
    return render(request, 'blog/seminar2_index.html', context)


def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = Author(name=form.cleaned_data['name'],
                            lastname=form.cleaned_data['surname'],
                            email=form.cleaned_data['email'],
                            bio=form.cleaned_data['bio'],
                            birthdate=form.cleaned_data['birthdate'])
            author.save()
            messages.add_message(request, messages.SUCCESS, 'Успешно')
    else:
        form = AuthorForm()
    return TemplateResponse(request, 'template_form.html', context={'form': form})


def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ArticleForm()
    return TemplateResponse(request, 'template_form.html', context={'form': form})


def authors_list(request):
    context = {'authors': Author.objects.all(), }
    return TemplateResponse(request, 'blog/template_authors_list.html', context)


def create_author_r(request):
    for i in range(random.randint(5, 10)):
        lname, fname, _ = fake.name().split()
        a = Author(name=fname, lastname=lname, email=fake.email(), bio=fake.text(), birthdate='2022-10-10')
        a.save()
    return redirect('authors_list')


def create_articles_r(request):
    a = Author.objects.all()
    for i in range(random.randint(15, 20)):
        title = 'Статья ' + str(i)
        text = fake.text()
        r = random.choice(a)
        article = Article(author_id=r, title=title, content=text, public_date=timezone.now(), cat='Статьи')
        article.save()
    return TemplateResponse(request, 'blog/template_authors_list.html')


def view_all_articles(request):
    articles = Article.objects.all()
    context = {'title': 'Список статей',
               'articles': articles}
    return TemplateResponse(request, 'blog/template_articles_list.html', context)


def view_article(request, id_article):
    article = Article.objects.get(pk=id_article)
    context = {'title': article.title,
               'text': article.content}
    article.show_count += 1
    article.save()
    return TemplateResponse(request, 'blog/template_article.html', context)
