# Generated by Django 2.0.13 on 2019-06-22 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0010_profile_problem_check'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='problem_check',
            field=models.CharField(default='1', max_length=200, null=True),
        ),
    ]
