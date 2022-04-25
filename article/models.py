from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from user_auth.models import PMEDUser

# class Author(models.Model):
#     first_name = models.CharField('First Name', max_length=100)
#     last_name = models.CharField('Last Name', max_length=100)
#     username = models.CharField('Username', max_length=100)
#     email = models.EmailField('Email')

#     def __str__(self):
#         return self.first_name + ' ' + self.last_name

class Article(models.Model):
    title = models.CharField('Title', max_length=255)
    slug = models.SlugField('Slug', max_length=255, unique=True)
    content = models.TextField('Content')
    status = models.BooleanField('Publish')
    author = models.ForeignKey(
        PMEDUser, on_delete=models.CASCADE, verbose_name='Author')
    created_at = models.DateTimeField('Writed At', auto_now_add=True)
    updated_at = models.DateField('Changed At', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

    def get_date(self):
        time = datetime.now()
        if self.created_at.day == time.day:
            return str(time.hour - self.created_at.hour) + " hours ago"
        else:
            if self.created_at.month == time.month:
                return str(time.day - self.created_at.day) + " days ago"
            else:
                if self.created_at.year == time.year:
                    return str(time.month - self.created_at.month) + " months ago"
        return self.created_at
        
    def get_absolute_url(self):
        return reverse('single', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.slug != slugify(self.title):
            self.slug = slugify(self.title)
        if not self.author:
            self.author = user.id
        return super().save(*args, **kwargs)
