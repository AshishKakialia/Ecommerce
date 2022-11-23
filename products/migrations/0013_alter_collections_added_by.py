# Generated by Django 4.1.3 on 2022-11-23 07:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0012_rename_user_collections_added_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collections',
            name='added_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
