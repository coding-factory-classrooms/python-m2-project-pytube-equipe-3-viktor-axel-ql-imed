import os

from django.core.management.base import BaseCommand
from django.utils import timezone
from ffmpy import FFmpeg

from API_Django import settings
from video import video_metadata
from video.models import Video, upload_file, id_generator
import concurrent.futures


class Command(BaseCommand):
    help = 'Create thumbnails for all videos'
    
    def create_thumbnail(self, video: Video):
        self.stdout.write(f'Trying to create a thumbnail for video={video}...')
        metadata: videoMetadata = video_metadata.extract_metadata(video.file.path)
        if metadata:
            base_url = 'https://pytube.s3.amazonaws.com/'
            suffix_url = video.__dict__['file']
            if not video.thumbnail:
                random_id = id_generator()
                file_key = random_id + ".png"
                ff = FFmpeg(
                    executable=r'D:\python-m2-project-pytube-equipe-3-viktor-axel-ql-imed\ffmpeg\bin\ffmpeg.exe',
                    inputs={base_url + suffix_url: None}, outputs={os.path.join(
                        settings.MEDIA_ROOT, file_key): ['-ss', '00:00:4', '-vframes', '1']})
                ff.run()
                print(os.path.join(settings.MEDIA_ROOT, file_key))

                file_path = os.path.join(settings.MEDIA_ROOT, file_key)
                args = {'ACL': 'public-read', 'ContentType': 'image/jpeg'}
                upload_file_key = "thumbnails/" + file_key
                upload_file(file_path, 'pytube', upload_file_key, args)
                video.thumbnail = upload_file_key
                video.save()
                os.remove(file_path)

    def handle(self, *args, **kwargs):
        # Lazy queryset
        # exécutée au dernier moment
        videos = Video.objects.exclude(thumbnail='')

        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            for video in videos:
                executor.submit(self.create_thumbnails, video)
            print(videos.__sizeof__())
        print('Finished!')
