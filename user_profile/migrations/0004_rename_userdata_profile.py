# Generated by Django 4.0.4 on 2022-06-06 10:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_profile', '0003_remove_userdata_password'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserData',
            new_name='Profile',
        ),
    ]
