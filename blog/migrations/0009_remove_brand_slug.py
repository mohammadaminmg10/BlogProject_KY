# Generated by Django 4.0.3 on 2022-04-29 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='slug',
        ),
    ]
