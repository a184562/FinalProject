# Generated by Django 3.2.18 on 2023-05-22 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='followings',
        ),
    ]
