# Generated by Django 2.0.dev20170426002136 on 2017-08-16 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_auto_20170816_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='current',
            field=models.BooleanField(help_text='Are you currently working at this position?', verbose_name='Yes'),
        ),
        migrations.AlterField(
            model_name='job',
            name='end_date',
            field=models.DateField(blank=True, verbose_name='When you stopped working'),
        ),
    ]