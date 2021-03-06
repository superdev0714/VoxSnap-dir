# Generated by Django 2.2.2 on 2019-06-20 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlexaLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AlexaSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('original_url', models.URLField(unique=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=4)),
                ('asin', models.CharField(max_length=64, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='GoogleAssistantAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField()),
                ('description', models.TextField()),
                ('original_url', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='GoogleAssistantDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=128)),
                ('system_name', models.CharField(max_length=64)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='VoiceApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('alexa_skill', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vad.AlexaSkill')),
                ('google_assistant_action', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vad.GoogleAssistantAction')),
            ],
        ),
        migrations.CreateModel(
            name='GoogleAssistantReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('username', models.CharField(max_length=64)),
                ('avatar_url', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vad.GoogleAssistantAction')),
            ],
        ),
        migrations.AddField(
            model_name='googleassistantaction',
            name='available_devices',
            field=models.ManyToManyField(to='vad.GoogleAssistantDevice'),
        ),
        migrations.AddField(
            model_name='googleassistantaction',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vad.Category'),
        ),
        migrations.CreateModel(
            name='AlexaSkillUtterance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('utterance', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vad.AlexaSkill')),
            ],
        ),
        migrations.AddField(
            model_name='alexaskill',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vad.Category'),
        ),
        migrations.AddField(
            model_name='alexaskill',
            name='supported_languages',
            field=models.ManyToManyField(to='vad.AlexaLanguage'),
        ),
        migrations.CreateModel(
            name='AlexaReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('title', models.CharField(max_length=128)),
                ('username', models.CharField(max_length=64)),
                ('text', models.TextField()),
                ('avatar_url', models.URLField()),
                ('found_helpful_count', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vad.AlexaSkill')),
            ],
        ),
    ]
