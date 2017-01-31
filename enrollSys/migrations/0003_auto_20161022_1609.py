# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrollSys', '0002_auto_20161021_0641'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_Student',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('course', models.ForeignKey(to='enrollSys.Course')),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='instructor',
        ),
        migrations.AlterField(
            model_name='student',
            name='fees_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='course_student',
            name='student',
            field=models.ForeignKey(to='enrollSys.Student'),
        ),
    ]
