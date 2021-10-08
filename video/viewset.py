from rest_framework import viewsets, generics
from rest_framework.response import Response

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

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.count_view += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class Video_tagViewSet(viewsets.ModelViewSet):
    queryset = Video_tag.objects.all()
    serializer_class = Video_tagSerializer
    lookup_field = 'tag'

