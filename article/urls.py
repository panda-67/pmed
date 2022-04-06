from django.urls import path

from . import views
from article.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<slug:slug>', SingleView.as_view(), name='single'),
    path('create/', CreateView.as_view(), name='create'),
    path('<int:pk>/update/', UpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', DestroyView.as_view(), name='destroy'),
]
