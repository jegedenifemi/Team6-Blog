from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
from  .models import Category, Post, SubCategory, Profile, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status')

class SummerAdmin(SummernoteModelAdmin):
    summernote_fields = ('contents',)
    list_display = ('title', 'author', 'status')


admin.site.register(Category)
admin.site.register(Post, SummerAdmin)
admin.site.register(SubCategory)
admin.site.register(Profile)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'email', 'publish','status')
    list_filter = ('status','publish')
    search_fields = ('name','email','content')
# admin.site.register()



