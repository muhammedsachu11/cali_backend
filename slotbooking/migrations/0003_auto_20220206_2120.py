# Generated by Django 2.2 on 2022-02-06 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slotbooking', '0002_auto_20220206_1953'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='SlotDetails',
            table='slot_time_details',
        ),
    ]