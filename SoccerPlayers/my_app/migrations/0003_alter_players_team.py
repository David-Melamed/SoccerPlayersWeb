# Generated by Django 3.2.12 on 2022-02-13 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_alter_teams_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='players',
            name='team',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
