# Generated by Django 2.2.2 on 2019-06-24 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vad', '0002_auto_20190623_2350'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlexaCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='alexaskill',
            name='is_free',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='alexalanguage',
            name='display_name',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]