# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comentario'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comentario',
            new_name='Mensajes',
        ),
    ]
