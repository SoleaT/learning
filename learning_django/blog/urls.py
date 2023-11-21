from django.urls import path

import blog.views

urlpatterns = [
    path('create_author',blog.views.create_author),
    path('create_author_random', blog.views.create_author_r, name='create_random_authors'),
    path('create_articles_r', blog.views.create_articles_r, name='create_random_articles'),
    path('create_article', blog.views.create_article, name='create_article'),
    path('list_authors', blog.views.authors_list, name='authors_list'),
    path('link_all_articles', blog.views.view_all_articles, name='view_all_articles'),
    path('view_article/<int:id_article>', blog.views.view_article, name='view_article'),
    path('', blog.views.seminar2)
]
