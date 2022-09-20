from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 100)


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


    def __str__(self):
        return self.name
    


class Tag(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    

class Profile(models.Model):
    pass


class Post(models.Model):
    choices = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    publish_on = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=choices, default= 'draft')
    contents = models.TextField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    tags = models.ForeignKey(Tag, on_delete = models.CASCADE)

    class Meta:
        ordering = ('-publish_on',)
    def __str__(self):
        return self.title