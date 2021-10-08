from rest_framework import viewsets

from video.models import Tag, Message, Video, Video_tag
from video.serializer import VideoSerializer, TagSerializer, MessageSerializer, Video_tagSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class Video_tagViewSet(viewsets.ModelViewSet):
    queryset = Video_tag.objects.all()
    serializer_class = Video_tagSerializer

    # @method_decorator(cache_page(60 * 20))
    # def dispatch(self, request, *args, **kwargs):
        # return super().dispatch(request, *args, **kwargs)