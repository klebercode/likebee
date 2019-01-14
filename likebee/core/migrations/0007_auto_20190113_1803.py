# Generated by Django 2.1.5 on 2019-01-13 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20190113_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priority',
            name='color',
            field=models.CharField(default='#666666', max_length=7, verbose_name='Cor'),
        ),
        migrations.AlterField(
            model_name='priority',
            name='color_text',
            field=models.CharField(choices=[('#ffffff', 'Branco'), ('#000000', 'Preto')], default='#ffffff', max_length=7, verbose_name='Cor do Texto'),
        ),
        migrations.AlterField(
            model_name='status',
            name='color',
            field=models.CharField(default='#666666', max_length=7, verbose_name='Cor'),
        ),
        migrations.AlterField(
            model_name='status',
            name='color_text',
            field=models.CharField(choices=[('#ffffff', 'Branco'), ('#000000', 'Preto')], default='#ffffff', max_length=7, verbose_name='Cor do Texto'),
        ),
    ]