# Generated by Django 5.1.7 on 2025-03-26 04:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0008_remove_order_address_remove_order_card_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="products",
        ),
        migrations.RemoveField(
            model_name="orderitem",
            name="card",
        ),
        migrations.RemoveField(
            model_name="orderitem",
            name="user",
        ),
    ]
