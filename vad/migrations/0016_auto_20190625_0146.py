# Generated by Django 2.2.2 on 2019-06-25 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vad', '0015_auto_20190625_0138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='googleassistantaction',
            name='details',
        ),
        migrations.AddField(
            model_name='googleassistantaction',
            name='icon_url',
            field=models.URLField(null=True, unique=True),
        ),
    ]
