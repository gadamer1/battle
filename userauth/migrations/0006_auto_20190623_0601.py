# Generated by Django 2.0.13 on 2019-06-22 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0005_auto_20190623_0601'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='check',
            new_name='problem_check',
        ),
    ]
