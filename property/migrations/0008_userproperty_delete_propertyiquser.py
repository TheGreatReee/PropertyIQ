# Generated by Django 4.1.7 on 2023-03-31 05:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0007_property_searchhistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_viewed', models.DateTimeField(auto_now=True)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.property')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'property')},
            },
        ),
        migrations.DeleteModel(
            name='PropertyIQUser',
        ),
    ]
