from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

class IndexView(TemplateView):
    template_name = "article/index.html"