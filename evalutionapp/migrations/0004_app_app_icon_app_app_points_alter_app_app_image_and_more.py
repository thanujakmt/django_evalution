# Generated by Django 5.1 on 2024-08-20 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evalutionapp', '0003_imageupload'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='app_icon',
            field=models.ImageField(default=0, upload_to='app_images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='app',
            name='app_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='app',
            name='app_image',
            field=models.ImageField(upload_to='app_images/'),
        ),
        migrations.DeleteModel(
            name='AppPoint',
        ),
    ]
