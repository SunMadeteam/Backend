# Generated by Django 4.0.1 on 2022-03-12 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_product_florist_alter_product_hight'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
