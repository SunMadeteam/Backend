# Generated by Django 4.0.1 on 2022-03-16 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_alter_order_delivery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delivery',
        ),
        migrations.AddField(
            model_name='delivery',
            name='order',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.order'),
        ),
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]