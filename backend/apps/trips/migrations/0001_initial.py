# Generated by Django 4.2.7 on 2023-12-13 08:45

import apps.trips.models
import customFields.compressed_image_field
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Новый выезд', max_length=100)),
                ('scheme', customFields.compressed_image_field.CompressedImageField(blank=True, null=True, quality=75, upload_to=apps.trips.models.get_scheme_path)),
                ('blurhash', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-updatedAt'],
            },
        ),
        migrations.CreateModel(
            name='TripDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dates', to='trips.trip')),
            ],
        ),
    ]
