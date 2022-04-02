# Generated by Django 4.0.1 on 2022-03-25 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_remove_cart_total_sum_remove_order_total_sum'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_sum',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cart_detail',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='order_detail',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]