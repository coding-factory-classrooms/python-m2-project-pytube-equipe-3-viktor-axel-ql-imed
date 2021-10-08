from rest_framework import serializers
from video.models import Video, Message, Tag, Video_tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class MessageSerializer(serializers.ModelSerializer):
    video_title = serializers.ReadOnlyField(source='video.title')

    class Meta:
        model = Message
        fields = ['id', 'text', 'video_title', 'posted']


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class Video_tagSerializer(serializers.ModelSerializer):
    video_title = serializers.ReadOnlyField(source='video.title')
    tag_name = serializers.ReadOnlyField(source='tag.name')

    class Meta:
        model = Video_tag
        fields = ['id', 'video_title', 'tag_name']

