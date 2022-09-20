from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
from  .models import Category, Post



class SummerAdmin(SummernoteModelAdmin):
    summernote_fields = ('contents',)


admin.site.register(Category)
admin.site.register(Post, SummerAdmin)
