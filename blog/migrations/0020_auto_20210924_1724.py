# Generated by Django 3.2.4 on 2021-09-24 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0019_auto_20210924_1038'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogs',
            options={'ordering': ['-created']},
        ),
        migrations.AlterField(
            model_name='blogs',
            name='writer',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
