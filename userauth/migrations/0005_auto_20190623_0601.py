# Generated by Django 2.0.13 on 2019-06-22 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0004_profile_check'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='check',
            field=models.CharField(default='', max_length=200),
        ),
    ]
