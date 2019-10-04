# Generated by Django 2.2.2 on 2019-06-24 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vad', '0008_auto_20190624_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alexaskillutterance',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='utterances', to='vad.AlexaSkill'),
        ),
        migrations.AlterUniqueTogether(
            name='alexaskillutterance',
            unique_together={('skill', 'utterance')},
        ),
    ]