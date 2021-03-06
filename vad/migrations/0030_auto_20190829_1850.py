# Generated by Django 2.2.2 on 2019-08-29 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vad', '0029_auto_20190827_0033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alexaskill',
            name='review',
        ),
        migrations.RemoveField(
            model_name='googleassistantaction',
            name='available_devices',
        ),
        migrations.AddField(
            model_name='alexareview',
            name='skill',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vad.AlexaSkill'),
        ),
        migrations.AlterField(
            model_name='voiceapp',
            name='alexa_skill',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vad.AlexaSkill'),
        ),
    ]
