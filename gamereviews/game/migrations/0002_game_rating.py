# Generated by Django 3.2.2 on 2021-06-17 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='rating',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
