# Generated by Django 3.2.8 on 2021-10-08 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_alter_video_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': [('test_change_task_status', 'test aarara  Can change the status of tasks'), ('test_close_task', 'Test Can removeaaaaaaa a task by setting its status as closed')],
            },
        ),
    ]