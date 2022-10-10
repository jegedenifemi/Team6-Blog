from django.forms import ModelForm
from django import forms
from post.models import Post, Comment, Profile
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.fields import SummernoteTextField
class PostForm(forms.ModelForm):
    # contents = SummernoteTextField()
    contents = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = Post
        fields = ['title', 'status', 'description','category','tags','contents']



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email','comment')


class ProfileForm(forms.ModelForm):
    class Meta:
        fields = ('avatar',)

