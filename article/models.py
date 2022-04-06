from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Author(models.Model):
    first_name = models.CharField('First Name', max_length=100)
    last_name = models.CharField('Last Name', max_length=100)
    username = models.CharField('Username', max_length=100)
    email = models.EmailField('Email')


class Article(models.Model):
    title = models.CharField('Title', max_length=255)
    slug = models.SlugField('Slug', max_length=255, unique=True)
    status = models.BooleanField('Publish')
    content = models.TextField('Content')
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, verbose_name='Author')
    created_at = models.DateField('Writed At', auto_now_add=True)
    updated_at = models.DateField('Changed At', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('single', kwargs={'slug' : self.slug})
