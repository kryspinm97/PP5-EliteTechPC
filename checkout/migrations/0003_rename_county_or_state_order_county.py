# Generated by Django 3.2.19 on 2023-06-23 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_order_country'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='county_or_state',
            new_name='county',
        ),
    ]