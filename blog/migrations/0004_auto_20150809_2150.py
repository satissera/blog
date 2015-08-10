# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150809_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensajes',
            name='mensaje',
            field=models.TextField(verbose_name='Mensaje'),
        ),
    ]
