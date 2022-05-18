from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['topic','owner','title', 'slug', 'publish', 'status','created', 'updated','status']