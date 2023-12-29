# Generated by Django 4.2.7 on 2023-12-13 08:45

import apps.points.models
import customFields.compressed_image_field
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trips', '0001_initial'),
        ('samples', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=8, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['createdAt'],
            },
        ),
        migrations.CreateModel(
            name='PointSample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=128)),
                ('point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='points.point')),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samples.sample')),
            ],
        ),
        migrations.CreateModel(
            name='PointPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', customFields.compressed_image_field.CompressedImageField(blank=True, null=True, quality=75, upload_to=apps.points.models.get_photo_point_path)),
                ('blurhash', models.CharField(blank=True, max_length=255, null=True)),
                ('point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='points.point')),
            ],
        ),
        migrations.AddField(
            model_name='point',
            name='samples',
            field=models.ManyToManyField(through='points.PointSample', to='samples.sample'),
        ),
        migrations.AddField(
            model_name='point',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='points', to='trips.trip'),
        ),
    ]
