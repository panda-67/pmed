from django.forms import ModelForm
from django import forms
from article.models import Article
from user_auth.models import PMEDUser

# Create the form class.
class ArticleForm(ModelForm):

    # form = author(initial={'PMEDUser': request.user})
    class Meta:
        model = Article
        fields = ['title', 'status', 'content', 'author']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-3'}),            
            'content': forms.Textarea(attrs={'class': 'form-control mb-3'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input mb-3', 'role': 'switch'}),
            'author': forms.HiddenInput()
        }
