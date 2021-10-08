from django.contrib.auth.models import User
from django.db import models

from . import video_metadata
from .validators import validate_file_extension


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
            metadata = video_metadata.extract_metadata(self.file.path)
            if metadata:
                self.duration = metadata.duration
        super().save(*args, **kwargs)


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
