from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

from . import video_metadata
from .validators import validate_file_extension
from ffmpy import FFmpeg
import urllib.request
import os
from API_Django import settings
import random
import string
import boto3
import requests
from django.conf import settings

BASE_DIR = 'https://pytube.s3.amazonaws.com/'


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


s3client = boto3.client('s3')


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class Video(models.Model):
    title = models.CharField(max_length=50)
    duration = models.IntegerField()
    file = models.FileField(blank=False, upload_to='VideoMP4', validators=[
        validate_file_extension])
    thumbnail = models.ImageField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    count_view = models.IntegerField(default=0)
    # creator = models.ForeignKey(User, on_delete=models.CASCADE)

    STATUS_DRAFT = 'draft'
    STATUS_PUBLISHED = 'published'
    STATUS_PRIVATE = 'private'
    STATUS_UNLISTED = 'unlisted'
    STATUS_CHOICES = [
        (STATUS_DRAFT, 'Brouillon'),            # Tuple
        (STATUS_PUBLISHED, 'Publié'),           # Tuple
        (STATUS_PRIVATE, 'Privé'),              # Tuple
        (STATUS_UNLISTED, 'Non repertorié'),    # Tuple
    ]
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=STATUS_DRAFT)

    def __str__(self):
        return self.title

    print('UPLOADING VIDEO')

    def save(self, *args, **kwargs):
        print('UPLOADING VIDEO function save')
        print(self)
        print(*args)
        print(**kwargs)
        print(self.duration)
        # print("Path",self.file.path)
        print("Name", self.file.name)
        # ff = FFmpeg( inputs={"https://pytube.s3.amazonaws.com/VideoMP4/Sample-MP4-Video-File-for-Testing_XJGTQsR.mp4": None}, outputs={"output.png": ['-ss', '00:00:4', '-vframes', '1']})
        # print(ff.cmd)
        # print('cmd should be printed')
        # ff.run()
        # ff
        # Code très difficile à tester
        # Il faut mocker beaucoup trop de choses
        # pour juste vérifier que le modèle est correctement mis à jour
        if not self.pk and self.file:
            metadata = video_metadata.extract_metadata(self.file.name)
            if metadata:
                self.duration = metadata.duration
        super().save(*args, **kwargs)


def extra_handle(self):
    print("EXTRA handling method can be called, here you could use another funnction to extract  with link")


def upload_file(file_name, bucket, object_name=None, args=None):
    if object_name is None:
        object_name = file_name
    response = s3client.upload_file(
        file_name, bucket, object_name, ExtraArgs=args)
    print(response)
    return response


def post_save_video_signal(sender, instance, created, raw, using, update_fields=None, **kwargs):
    print('coco on passe ici')
    print('\n')
    print(created)
    print(raw)
    print("Sender", sender)
    base_url = 'https://pytube.s3.amazonaws.com/'
    suffix_url = instance.__dict__['file']
    if not instance.thumbnail:
        random_id = id_generator()
        file_key = random_id+".png"
        file_path = os.path.join(settings.MEDIA_ROOT, file_key)
     

        # print(data)
        # print("\n")
        print('filepath')
        print(file_path)
        ff = FFmpeg(inputs={base_url+suffix_url: None}, outputs={file_path: ['-ss', '00:00:4', '-vframes', '1']})
        ff.run()
        print(file_path)
        args = {'ACL': 'public-read', 'ContentType': 'image/jpeg'}
        upload_file_key = "thumbnails/" + file_key
        upload_file(file_path, 'pytube', upload_file_key, args)
        instance.thumbnail = upload_file_key
        instance.save()
        os.remove(file_path)



class Message(models.Model):
    text = models.CharField(max_length=100)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    # transmitter

    def __str__(self):
        return self.text


class Video_tag(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class TestTask(models.Model):
    class Meta:
        # ces permissions là sont add que si leur identifiant n'existe pas déjà
        permissions = [
            ("test_1-2", "test 1 2"),
            ("test_3_4", "Test 3 4"),
        ]


post_save.connect(post_save_video_signal, sender=Video)
