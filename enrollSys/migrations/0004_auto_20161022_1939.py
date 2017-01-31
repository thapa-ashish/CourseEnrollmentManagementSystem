# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrollSys', '0003_auto_20161022_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='course',
        ),
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(default=1, to='enrollSys.Instructor'),
            preserve_default=False,
        ),
    ]
