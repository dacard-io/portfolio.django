# Generated by Django 2.0.dev20170426002136 on 2017-08-13 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_remove_project_testfield'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
    ]