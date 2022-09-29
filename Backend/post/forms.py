from django.forms import ModelForm
from django import forms
from post.models import Post
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.fields import SummernoteTextField
class PostForm(forms.ModelForm):
    # contents = SummernoteTextField()
    contents = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = Post
        fields = ['title', 'status', 'description','category','tags','contents']