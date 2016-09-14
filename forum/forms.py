from django import forms
from django.contrib.auth.models import User

from .models import Forum, Comment


class ForumForm(forms.ModelForm):

    class Meta:
        model = Forum
        fields = ['article_title', 'article_subject', 'article_body']



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # owner = request.user
        fields = ['forum_comment']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']