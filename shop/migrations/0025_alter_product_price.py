# Generated by Django 4.0.1 on 2022-04-02 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_remove_delivery_adress_order_adress_order_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
