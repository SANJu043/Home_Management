# Generated by Django 5.2 on 2025-04-27 06:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_item_inventoryitem_alter_calendarevent_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendarevent',
            name='time',
            field=models.TimeField(default=datetime.datetime(2025, 4, 27, 6, 32, 23, 433028, tzinfo=datetime.timezone.utc)),
        ),
    ]
