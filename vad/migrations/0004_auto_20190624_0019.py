# Generated by Django 2.2.2 on 2019-06-24 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vad', '0003_auto_20190624_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alexacategory',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]