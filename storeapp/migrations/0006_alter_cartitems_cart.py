# Generated by Django 5.0.6 on 2024-06-29 16:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0005_alter_cartitems_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitems',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='itemsss', to='storeapp.cart'),
        ),
    ]