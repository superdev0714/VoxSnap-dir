# Generated by Django 2.2.2 on 2019-06-24 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vad', '0013_auto_20190624_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alexareview',
            name='username',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
