# Generated by Django 5.1.7 on 2025-04-03 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='photo',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
