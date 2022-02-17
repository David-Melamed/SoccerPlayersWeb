# Generated by Django 3.2.12 on 2022-02-13 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_teams_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='players',
            name='picture',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]