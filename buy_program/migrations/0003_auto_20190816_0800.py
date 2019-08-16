# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-16 08:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy_program', '0002_auto_20190805_2028'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.DecimalField(decimal_places=2, max_digits=3)),
                ('weight', models.PositiveIntegerField(default=0)),
                ('age', models.PositiveIntegerField(default=0)),
                ('levels', models.CharField(choices=[('Begginer', 'Begginer'), ('Medium', 'Medium'), ('Advance', 'Advance')], default='Begginer', max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='your_details',
        ),
    ]