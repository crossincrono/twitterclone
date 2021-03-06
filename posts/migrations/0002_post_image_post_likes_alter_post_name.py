# Generated by Django 4.0.4 on 2022-05-11 22:20

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, db_index=True, max_length=255, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.PositiveBigIntegerField(blank=True, db_index=True, default=0, verbose_name='like'),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(db_index=True, default='Annoymous', max_length=140, verbose_name='Name'),
        ),
    ]
