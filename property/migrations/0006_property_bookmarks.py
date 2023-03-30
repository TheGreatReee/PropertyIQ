# Generated by Django 4.1.7 on 2023-03-30 06:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0005_alter_property_latitude_alter_property_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='bookmarks',
            field=models.ManyToManyField(blank=True, default=None, related_name='bookmark', to=settings.AUTH_USER_MODEL),
        ),
    ]
