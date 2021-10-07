from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.name}'


class Video(models.Model):
    title = models.CharField(max_length=50)
    duration = models.IntegerField()
    file = models.FileField(blank=False)
    thumbnail = models.ImageField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    STATUS_DRAFT = 'draft'
    STATUS_PUBLISHED = 'published'
    STATUS_PRIVATE = 'private'
    STATUS_UNLISTED = 'unlisted'
    STATUS_CHOICES = [
        (STATUS_DRAFT, 'Brouillon'),          # Tuple
        (STATUS_PUBLISHED, 'Publié'),         # Tuple
        (STATUS_PRIVATE, 'Privé'),            # Tuple
        (STATUS_UNLISTED, 'Non repertorié'),  # Tuple
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=STATUS_DRAFT)

    def __str__(self) -> str:
        return f'{self.title}'


class Message(models.Model):
    text = models.CharField(max_length=100)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    posted = models.DateTimeField(auto_now_add=True)
    # transmitter

    def __str__(self) -> str:
        return f'{self.id}'


class Video_tag(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
