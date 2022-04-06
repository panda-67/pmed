from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from article.models import Article


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

class IndexView(ListView):
    model = Article
    queryset = Article.objects.filter(status='1')
    context_object_name = 'articles'
    template_name = "article/index.html"


class CreateView(CreateView):
    model = Article
    fields = [
        'title',
        'slug',
        'status',
        'content',
        'author'
    ]
    success_url = reverse_lazy('index')
    template_name = "article/create.html"


class SingleView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = "article/single.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(status='1')[:5]
        return context


class UpdateView(UpdateView):
    model = Article
    fields = [
        'title',
        'slug',
        'status',
        'content',
        'author'
    ]
    template_name = "article/update.html"


class DestroyView(DeleteView):
    model = Article
    success_url = reverse_lazy('index')
