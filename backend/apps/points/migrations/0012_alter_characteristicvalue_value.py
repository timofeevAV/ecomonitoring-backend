# Generated by Django 4.2.7 on 2023-12-17 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0011_characteristicvalue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characteristicvalue',
            name='value',
            field=models.CharField(max_length=128),
        ),
    ]
