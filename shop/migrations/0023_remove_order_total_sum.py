# Generated by Django 4.0.1 on 2022-03-25 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0022_order_total_sum_alter_cart_detail_quantity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total_sum',
        ),
    ]
