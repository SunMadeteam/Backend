# Generated by Django 3.2.7 on 2022-02-08 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='salary',
            field=models.IntegerField(default=None),
        ),
    ]
