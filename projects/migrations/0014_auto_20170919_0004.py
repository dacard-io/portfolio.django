# Generated by Django 2.0.dev20170426002136 on 2017-09-19 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_auto_20170919_0003'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ('order',)},
        ),
        migrations.RenameField(
            model_name='project',
            old_name='my_order',
            new_name='order',
        ),
    ]