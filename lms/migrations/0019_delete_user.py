# Generated by Django 3.1.4 on 2021-01-08 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0018_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]