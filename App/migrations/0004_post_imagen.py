# Generated by Django 4.0.3 on 2022-04-18 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagen',
            field=models.ImageField(null=True, upload_to='posteos'),
        ),
    ]
