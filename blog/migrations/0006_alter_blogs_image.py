# Generated by Django 3.2.4 on 2021-09-16 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blogs_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
