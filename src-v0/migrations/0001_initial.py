# Generated by Django 3.1.5 on 2021-08-02 20:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='meval_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_text', models.CharField(max_length=100)),
                ('url_text', models.CharField(max_length=16)),
                ('created', models.DateTimeField(auto_now_add=True, help_text='timestamp of creation')),
                ('updated', models.DateTimeField(auto_now=True, help_text='timestamp of last update')),
            ],
        ),
        migrations.CreateModel(
            name='meval_module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_text', models.CharField(max_length=100)),
                ('url_text', models.CharField(max_length=16)),
                ('priority', models.IntegerField()),
                ('meval_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mmr.meval_category')),
            ],
        ),
        migrations.CreateModel(
            name='meval_question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_text', models.CharField(max_length=1000)),
                ('priority', models.IntegerField()),
                ('meval_module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mmr.meval_module')),
            ],
        ),
        migrations.CreateModel(
            name='meval_reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_text', models.CharField(max_length=1000)),
                ('priority', models.IntegerField()),
                ('score', models.IntegerField(default=0)),
                ('meval_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mmr.meval_question')),
            ],
        ),
        migrations.CreateModel(
            name='mreferral_purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_uniqid', models.CharField(max_length=100)),
                ('random_string_32', models.CharField(max_length=33)),
                ('terms_accepted', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, help_text='timestamp of creation')),
                ('meval_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mmr.meval_category')),
                ('muser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='meval_userscorerecommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_text', models.CharField(max_length=100)),
                ('priority', models.IntegerField()),
                ('score_low', models.IntegerField()),
                ('score_high', models.IntegerField()),
                ('meval_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mmr.meval_category')),
            ],
        ),
        migrations.CreateModel(
            name='meval_useranswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meval_question_id', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True, help_text='timestamp of creation')),
                ('updated', models.DateTimeField(auto_now=True, help_text='timestamp of last update')),
                ('meval_reply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mmr.meval_reply')),
                ('mmeval_module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mmr.meval_module')),
                ('mreferral_purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mmr.mreferral_purchase')),
            ],
            options={
                'unique_together': {('mreferral_purchase', 'meval_question_id')},
            },
        ),
    ]
