# Generated by Django 3.1.4 on 2021-01-04 09:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0005_auto_20210104_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lmsmodel',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='lmsmodel',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
