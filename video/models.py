from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

from . import video_metadata
from .validators import validate_file_extension
from ffmpy import FFmpeg
from django.conf import settings

BASE_DIR = 'https://pytube.s3.amazonaws.com/' # settings.BASE_DIR


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Video(models.Model):
    title = models.CharField(max_length=50)
    duration = models.IntegerField()
    file = models.FileField(blank=False, upload_to='VideoMP4', validators=[validate_file_extension])
    thumbnail = models.ImageField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    count_view = models.IntegerField(default=0)
    # creator = models.ForeignKey(User, on_delete=models.CASCADE)

    STATUS_DRAFT = 'draft'
    STATUS_PUBLISHED = 'published'
    STATUS_PRIVATE = 'private'
    STATUS_UNLISTED = 'unlisted'
    STATUS_CHOICES = [
        (STATUS_DRAFT, 'Brouillon'),  # Tuple
        (STATUS_PUBLISHED, 'Publié'),  # Tuple
        (STATUS_PRIVATE, 'Privé'),  # Tuple
        (STATUS_UNLISTED, 'Non repertorié'),  # Tuple
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=STATUS_DRAFT)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Code très difficile à tester
        # Il faut mocker beaucoup trop de choses
        # pour juste vérifier que le modèle est correctement mis à jour
        if not self.pk and self.file:
            metadata = video_metadata.extract_metadata(self.file.name)
            if metadata:
                self.duration = metadata.duration
        super().save(*args, **kwargs)


def post_save_video_signal(sender, instance, created, raw, using, update_fields=None, **kwargs):
    if not instance.thumbnail:
        ff = FFmpeg(executable='C:/projets-info/python-m2-project-pytube-equipe-3-viktor-axel-ql-imed/ffmpeg/bin'
                               '/ffmpeg.exe',
                    inputs={str(BASE_DIR) + str(instance.file.name): None},
                    outputs={"output.png": ['-ss', '00:00:4', '-vframes', '1']}) #if output.png exists, delete it and it works

        ff.run()

        instance.thumbnail = 'ouput.png'

        Video.save(instance)


class Message(models.Model):
    text = models.CharField(max_length=100)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    posted = models.DateTimeField(auto_now_add=True)

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
