# Generated by Django 4.1.3 on 2022-11-14 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_address_address_type_address_locality'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='address',
            new_name='building',
        ),
    ]
