import datetime

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=70)
    lastname = models.CharField(max_length=70)
    email = models.EmailField()
    bio = models.TextField()
    birthdate = models.DateField()

    def get_fullname(self):
        return f"{self.name} {self.lastname}"

    def __str__(self):
        return self.get_fullname()


class Article(models.Model):
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    public_date = models.DateField()
    show_count = models.IntegerField(default=0)
    published = models.BooleanField(default=False)


class Comment(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=200)
    comment_text = models.TextField(max_length=800)
    date_created = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)
