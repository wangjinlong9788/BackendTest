# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-29 20:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RecipeModel', '0005_auto_20190829_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='userModel.UserModel'),
        ),
    ]
