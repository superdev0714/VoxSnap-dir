# Generated by Django 2.2.5 on 2019-10-03 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vad', '0038_auto_20191003_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alexaskill',
            name='supported_languages',
        ),
        migrations.AddField(
            model_name='alexaskill',
            name='supported_languages',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vad.AlexaLanguage'),
        ),
    ]
