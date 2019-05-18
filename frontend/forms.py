from django import forms
from movie.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('movie', 'user', 'rate', 'comment')
