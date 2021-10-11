from rest_framework import viewsets, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import AnonymousUser
from video.models import Tag, Message, Video, Video_tag
from video.serializer import VideoSerializer, TagSerializer, MessageSerializer, Video_tagSerializer
from django.db.models.signals import post_save


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    print('view set called')
    def retrieve(self, request, *args, **kwargs):
        print('------- fonction "retrievce" dans VideoViewSet-------')
        instance = self.get_object()
        instance.count_view += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_permissions(self):
        if self.action == 'retrieve' or self.action == 'list':
            return [AllowAny(), ]
        return super().get_permissions()



class Video_tagViewSet(viewsets.ModelViewSet):
    queryset = Video_tag.objects.all()
    serializer_class = Video_tagSerializer
    lookup_field = 'tag'

def post_save_video_signal(sender, instance, created, raw, using, update_fields=None, **kwargs):
    print('From viewset')  
    print("Instance",instance.__dict__)
post_save.connect(post_save_video_signal, sender=Video)
