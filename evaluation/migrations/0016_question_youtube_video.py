# Generated by Django 2.2.7 on 2019-11-29 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0015_auto_20191127_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='youtube_video',
            field=models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Youtube Video (Will Replace Image)'),
        ),
    ]
