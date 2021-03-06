# Generated by Django 2.2.2 on 2019-09-10 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vad', '0033_auto_20190910_0513'),
    ]

    operations = [
        migrations.AddField(
            model_name='alexadevice',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='alexadevice',
            name='name',
            field=models.CharField(default='Alexa Device', max_length=128),
        ),
        migrations.AddField(
            model_name='alexadevice',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4),
        ),
        migrations.AddField(
            model_name='device',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='name',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='device',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4),
        ),
        migrations.AddField(
            model_name='googleassistantdevice',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='googleassistantdevice',
            name='name',
            field=models.CharField(default='Google Device', max_length=128),
        ),
        migrations.AddField(
            model_name='googleassistantdevice',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4),
        ),
    ]
