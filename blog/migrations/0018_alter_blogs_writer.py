# Generated by Django 3.2.4 on 2021-09-24 04:29

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_alter_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='writer',
            field=models.CharField(max_length=200, null=True, verbose_name=django.contrib.auth.models.User),
        ),
    ]
