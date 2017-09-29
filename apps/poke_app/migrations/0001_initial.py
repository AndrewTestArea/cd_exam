# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-28 23:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_app', '0007_auto_20170928_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poke',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('giver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gave', to='login_app.User')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='got', to='login_app.User')),
            ],
        ),
    ]
