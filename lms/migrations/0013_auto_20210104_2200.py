# Generated by Django 3.1.4 on 2021-01-04 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0012_auto_20210104_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lmsmodel',
            name='date',
            field=models.DateTimeField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='lmsmodel',
            name='time',
            field=models.DateTimeField(blank=True, default='', null=True),
        ),
    ]