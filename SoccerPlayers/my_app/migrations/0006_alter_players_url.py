# Generated by Django 3.2.12 on 2022-02-16 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_auto_20220214_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='players',
            name='url',
            field=models.URLField(blank=True, max_length=255),
        ),
    ]