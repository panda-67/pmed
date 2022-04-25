from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from article.models import Article
from article.form import ArticleForm
from django.http import request


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

class IndexView(ListView):
    model = Article
    queryset = Article.objects.filter(status='1')
    context_object_name = 'articles'
    template_name = "article/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['unpublish'] = Article.objects.filter(status='0')
        context['active'] = 'index'
        return context


class SingleView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = "article/single.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(status='1')[:5]
        return context


class CreateView(FormView):
    form_class = ArticleForm
    success_url = reverse_lazy('index')
    template_name = "article/create.html"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'create'
        return context


class UpdateView(UpdateView):
    model = Article
    context_object_name = 'article'
    form_class = ArticleForm
    template_name = "article/update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'create'
        return context

class DestroyView(DeleteView):
    model = Article
    success_url = reverse_lazy('index')
