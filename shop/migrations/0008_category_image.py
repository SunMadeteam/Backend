# Generated by Django 4.0.1 on 2022-03-01 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_remove_order_detail_cart_order_detail_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.TextField(default=None, null=True),
        ),
    ]
