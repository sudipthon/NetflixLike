# Generated by Django 4.2.1 on 2023-05-31 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_videoproxy_video_active_video_video_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videoproxy',
            options={'verbose_name': 'Published Video', 'verbose_name_plural': 'Published Videos'},
        ),
    ]