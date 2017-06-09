# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 10:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('birthDate', models.DateTimeField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Unknow')], default='U', max_length=1)),
                ('weight', models.CharField(choices=[('L', 'Light'), ('M', 'Medium'), ('H', 'Heavy')], default='M', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Circuit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('nb_laps', models.IntegerField(default=3)),
                ('img_url', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Cup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img_url', models.CharField(max_length=500)),
                ('retro', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('abbreviation', models.CharField(max_length=10)),
                ('platform', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('character', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.Character')),
                ('hours', models.IntegerField(default=0)),
                ('avg_position', models.IntegerField(default=8)),
                ('nb_use', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='cup',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cups', to='api.Game'),
        ),
        migrations.AddField(
            model_name='circuit',
            name='cup',
            field=models.ManyToManyField(to='api.Cup'),
        ),
    ]
