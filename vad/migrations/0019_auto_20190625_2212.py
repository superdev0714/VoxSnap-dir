# Generated by Django 2.2.2 on 2019-06-25 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vad', '0018_auto_20190625_0212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='googleassistantaction',
            name='privacy_policy_url',
            field=models.URLField(null=True),
        ),
    ]
