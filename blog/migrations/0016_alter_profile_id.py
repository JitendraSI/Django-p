# Generated by Django 3.2.4 on 2021-09-21 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.IntegerField(editable=False, primary_key=True, serialize=False),
        ),
    ]
