# Generated by Django 4.2.7 on 2023-12-13 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pointsample',
            name='value',
        ),
    ]
