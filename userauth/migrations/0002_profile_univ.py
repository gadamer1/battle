# Generated by Django 2.0.13 on 2019-06-22 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='univ',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
