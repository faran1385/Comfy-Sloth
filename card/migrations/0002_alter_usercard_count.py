# Generated by Django 4.2 on 2023-06-13 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercard',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]