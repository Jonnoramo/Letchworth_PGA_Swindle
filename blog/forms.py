from django import forms
from .models import PostBlog

class BlogPostForm(forms.ModelForm):

    class Meta:
        model = PostBlog
        fields = ('title', 'content', 'image')