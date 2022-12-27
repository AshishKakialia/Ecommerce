# Generated by Django 4.1.4 on 2022-12-27 13:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title of product', max_length=50)),
                ('description', models.CharField(default='description of product', max_length=500)),
                ('price', models.CharField(default=100, max_length=10)),
                ('image', models.ImageField(null=True, upload_to='home_images')),
                ('product_category', models.CharField(choices=[('Fashion', 'fashion'), ('Gadgets', 'gadgets'), ('Home', 'home'), ('Electronics', 'electronics')], default='random', max_length=20)),
            ],
            options={
                'verbose_name': 'Product',
            },
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.products')),
            ],
            options={
                'verbose_name': 'home',
            },
        ),
        migrations.CreateModel(
            name='Gadgets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gadgets_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.products')),
            ],
            options={
                'verbose_name': 'Gadget',
            },
        ),
        migrations.CreateModel(
            name='Fashion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fashion_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.products')),
            ],
            options={
                'verbose_name': 'fashion',
            },
        ),
        migrations.CreateModel(
            name='Electronics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('electronics_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.products')),
            ],
            options={
                'verbose_name': 'Electronic',
            },
        ),
        migrations.CreateModel(
            name='Collections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('added_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.products')),
            ],
            options={
                'verbose_name': 'Collection',
            },
        ),
    ]
