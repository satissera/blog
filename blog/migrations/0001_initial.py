# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100, verbose_name='T\xedtulo')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha del Post')),
                ('resumen', models.CharField(max_length=512, verbose_name='Resumen')),
                ('contenido', models.TextField(verbose_name='Contenido')),
            ],
            options={
                'ordering': ['-fecha'],
                'verbose_name': 'Mi Entrada',
                'verbose_name_plural': 'Todas mis entradas',
            },
        ),
    ]
