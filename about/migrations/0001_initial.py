# Generated by Django 4.2 on 2023-06-05 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35)),
                ('img', models.ImageField(upload_to='./media/about/')),
                ('discription', models.CharField(max_length=1024)),
            ],
        ),
    ]