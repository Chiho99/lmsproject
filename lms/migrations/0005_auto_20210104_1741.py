# Generated by Django 3.1.4 on 2021-01-04 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0004_auto_20210104_1727'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lmsmodel',
            old_name='finish',
            new_name='time',
        ),
        migrations.RemoveField(
            model_name='lmsmodel',
            name='start',
        ),
    ]