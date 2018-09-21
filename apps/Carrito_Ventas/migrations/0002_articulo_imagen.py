# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Carrito_Ventas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='imagen',
            field=models.ImageField(default=datetime.datetime(2018, 9, 21, 3, 25, 9, 965000, tzinfo=utc), upload_to=b'Articulo'),
            preserve_default=False,
        ),
    ]
