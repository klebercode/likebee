# Generated by Django 2.1.5 on 2019-01-31 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20190130_2206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='priority',
            name='done',
        ),
    ]
