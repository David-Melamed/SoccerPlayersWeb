# Generated by Django 3.2.12 on 2022-02-13 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
