# Generated by Django 4.0.1 on 2022-02-17 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart_detail',
            old_name='cart_id',
            new_name='cart',
        ),
        migrations.RenameField(
            model_name='order_detail',
            old_name='cart_id',
            new_name='cart',
        ),
        migrations.AddField(
            model_name='order',
            name='delivery',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.delivery'),
        ),
    ]