# Generated by Django 4.2.7 on 2023-12-18 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(max_length=128),
        ),
    ]
