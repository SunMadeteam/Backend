# Generated by Django 4.0.1 on 2022-03-25 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_alter_cart_total_sum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='total_sum',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total_sum',
        ),
    ]
