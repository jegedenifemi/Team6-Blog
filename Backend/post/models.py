from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model
from random import randint
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.



User = get_user_model()
class Category(models.Model):
    name = models.CharField(max_length = 100, unique=True, null=True)
    category_slug = models.SlugField(max_length = 100, unique= True, blank =True, null = True)


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.category_slug = slugify(str(self.name))
        super(Category, self).save(*args, **kwargs)

    def get_cat():
        results, _ = Category.objects.get_or_create(name='Generic')
        return results.pk


class SubCategory(models.Model):
    name = models.CharField(max_length = 100, unique=True, null=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, blank =True, null = True)
    sub_category_slug = models.SlugField(max_length = 100, unique= True, blank =True, null = True)


    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.sub_category_slug = slugify(str(self.name))
        super(SubCategory, self).save(*args, **kwargs)

    def get_sub():
        results, _ = SubCategory.objects.get_or_create(name='generic')
        return results.pk



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
    image = models.ImageField(upload_to='post/%d/%m/%y',default =  'post/faf75719-9275-4348-b2e1-269eeb2c023b.png')
    status = models.CharField(max_length=20, choices=choices, default= 'draft')
    contents = models.TextField()
    description = models.TextField(blank = True)
    bookmarks = models.ManyToManyField(User, related_name='bookmark',default=None, blank=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, default=Category.get_cat, blank =True, null = True)
    sub_category = models.ForeignKey(SubCategory, on_delete = models.CASCADE, default = SubCategory.get_sub, blank =True, null = True)
    tags = TaggableManager(blank=True)

    class Meta:
        ordering = ('-publish_on',)
        
    def __str__(self):
        return self.title

    
   
    def save(self, *args, **kwargs):
        mySlug = str(self.category) + str('/') + str(self.title)
        self.slug = slugify(mySlug)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('post:post_detail', kwargs={'slug': self.slug})




class Profile(models.Model):

    # class PostObjects(models.Manager):
    #     def get_queryset(self):
    #         queryset = super(Post, self).get_queryset().filter(self.blogger = self.posts.author)
            
    #         return queryset
    blogger = models.OneToOneField(User, on_delete = models.CASCADE, default = 1)
    # posts = models.ForeignKey(Post, on_delete=models.CASCADE)
    # bio = models.TextField(max_length = 250)
    avatar = models.ImageField(default = '/images/profile_pics/pngfind.com-placeholder-png-6104451.png',blank = True, null = True, upload_to='images/profile_pics')

@ receiver(post_save, sender = User)
def create_user_profile(sender, instance, created,**kwargs):
    if created:
        Profile.objects.create(blogger=instance)




class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'comments')
    comment = models.TextField(max_length = 10000,null=True)
    email = models.EmailField()
    publish = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length = 50)
    status = models.BooleanField(default = True)


    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return f"comment by {self.name} on {self.post}"

class Bookmarks(models.Model):
    pass

