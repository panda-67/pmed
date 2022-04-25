from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from article.views import *

urlpatterns = [
    path('', login_required(IndexView.as_view()), name='index'),
    path('<slug:slug>', SingleView.as_view(), name='single'),
    path('create/', login_required(CreateView.as_view()), name='create'),
    path('<int:pk>/update/', login_required(UpdateView.as_view()), name='update'),
    path('<int:pk>/delete/', login_required(DestroyView.as_view()), name='destroy'),
]
