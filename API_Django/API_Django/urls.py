from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from video.viewset import TagViewSet, MessageViewSet, VideoViewSet, Video_tagViewSet
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register(r'tag', TagViewSet)
router.register(r'message', MessageViewSet)
router.register(r'video', VideoViewSet)
router.register(r'video_tag', Video_tagViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
]
