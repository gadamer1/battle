# Generated by Django 2.0.13 on 2019-06-22 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0006_auto_20190623_0601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='problem_check',
            field=models.CharField(max_length=200),
        ),
    ]