# Generated by Django 5.1.1 on 2024-11-24 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='genre',
            field=models.CharField(default='action', max_length=200),
        ),
    ]
