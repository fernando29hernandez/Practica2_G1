# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Carrito_Ventas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seccion',
            name='created_at',
        ),
    ]
