from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
from  .models import Tag, Category, Post



class SummerAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Post, SummerAdmin)
