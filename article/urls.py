from django.urls import path

from . import views
from article.views import *

urlpatterns = [
    path('', IndexView.as_view()),
]