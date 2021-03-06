# Generated by Django 2.2.2 on 2019-06-25 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vad', '0014_auto_20190624_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='googleassistantdevice',
            name='system_name',
        ),
        migrations.AddField(
            model_name='googleassistantaction',
            name='image_url',
            field=models.URLField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='googleassistantaction',
            name='name',
            field=models.CharField(default=None, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='googleassistantaction',
            name='privacy_policy_url',
            field=models.URLField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='googleassistantaction',
            name='system_name',
            field=models.CharField(default=None, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='googleassistantdevice',
            name='image_url',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='googleassistantaction',
            name='original_url',
            field=models.URLField(unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='googleassistantaction',
            unique_together={('system_name', 'original_url')},
        ),
        migrations.CreateModel(
            name='GoogleAssistantUtterance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('utterance', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='utterances', to='vad.GoogleAssistantAction')),
            ],
            options={
                'unique_together': {('action', 'utterance')},
            },
        ),
    ]
