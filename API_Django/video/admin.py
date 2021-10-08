from django.contrib import admin
from .models import Tag, Video, Message, Video_tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'duration', 'file', 'thumbnail', 'created', 'status']
    search_fields = ['title']
    list_filter = ('status',)  #Tuple


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'video', 'posted']


@admin.register(Video_tag)
class Video_tagAdmin(admin.ModelAdmin):
    list_display = ['id', 'video', 'tag']