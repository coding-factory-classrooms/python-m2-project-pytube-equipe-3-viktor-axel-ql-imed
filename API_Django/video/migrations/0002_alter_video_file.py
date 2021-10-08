# Generated by Django 3.2.8 on 2021-10-08 09:49

from django.db import migrations, models
import video.validators


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.FileField(upload_to='VideoMP4', validators=[video.validators.validate_file_extension]),
        ),
    ]
