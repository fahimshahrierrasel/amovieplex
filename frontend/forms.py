from django import forms
from django.contrib.auth.forms import UserCreationForm

from movie.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('movie', 'user', 'rate', 'comment')
