# Generated by Django 3.2.7 on 2021-11-29 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='abc', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
