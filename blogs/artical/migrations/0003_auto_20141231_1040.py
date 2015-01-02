# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artical', '0002_auto_20141231_1029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='question_content',
            new_name='post_content',
        ),
    ]
