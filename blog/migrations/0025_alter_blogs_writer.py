# Generated by Django 3.2.4 on 2021-09-24 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_alter_blogs_writer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='writer',
            field=models.CharField(default='@writersname', max_length=200),
        ),
    ]
