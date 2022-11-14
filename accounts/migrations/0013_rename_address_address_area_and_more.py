# Generated by Django 4.1.3 on 2022-11-14 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_address_address_alter_address_address_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='address',
            new_name='Area',
        ),
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(choices=[('home', 'Home'), ('office', 'Office'), ('other', 'Other')], default='Home', max_length=20),
        ),
    ]
