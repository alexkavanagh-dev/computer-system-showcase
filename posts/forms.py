from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author', 'slug', 'likes', 'created_on',
                   'updated_on', 'featured_post',)
