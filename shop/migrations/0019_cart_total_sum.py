# Generated by Django 4.0.1 on 2022-03-24 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_remove_cart_total_sum_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total_sum',
            field=models.IntegerField(default=0),
        ),
    ]