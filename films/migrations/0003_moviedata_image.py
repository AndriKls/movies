# Generated by Django 5.1.1 on 2024-11-24 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_moviedata_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='image',
            field=models.ImageField(default='Images/None/Noimg.jpg', upload_to='Images/'),
        ),
    ]
