# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Carrito_Ventas', '0002_articulo_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='imagen',
            field=models.ImageField(null=True, upload_to=b'Articulo'),
        ),
    ]
