# Generated by Django 4.1.3 on 2022-11-28 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0013_alter_collections_added_by"),
    ]

    operations = [
        migrations.AlterField(
            model_name="products",
            name="product_category",
            field=models.CharField(
                choices=[
                    ("Fashion", "fashion"),
                    ("Gadgets", "gadgets"),
                    ("Home", "home"),
                    ("Electronics", "electronics"),
                ],
                default="random",
                max_length=20,
            ),
        ),
    ]
