# Generated by Django 3.1.4 on 2021-01-07 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0016_auto_20210107_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goalmodel',
            name='goal',
            field=models.IntegerField(null=True),
        ),
    ]