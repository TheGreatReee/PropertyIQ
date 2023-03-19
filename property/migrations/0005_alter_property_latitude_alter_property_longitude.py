# Generated by Django 4.1.7 on 2023-03-12 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_rename_x_coordinates_property_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=20, null=True),
        ),
    ]