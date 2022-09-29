from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model
from random import randint
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 100)


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


    def __str__(self):
        return self.name
    


User = get_user_model()
class Profile(models.Model):
    pass


class Post(models.Model):
    choices = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=500, unique = True)
    slug = models.SlugField(max_length=200, unique=True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    publish_on = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=choices, default= 'draft')
    contents = models.TextField()
    description = models.TextField(blank = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish_on',)
        
    def __str__(self):
        return self.title

    
    # whenever the post is edited the slug changes, this needs to be fixed
    
    def save(self, *args, **kwargs):
        mySlug = str(self.category) + '//' + self.title
        self.slug = slugify(mySlug)
        super(Post, self).save(*args, **kwargs)
