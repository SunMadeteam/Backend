# Generated by Django 4.0.1 on 2022-04-02 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_alter_user_salary_delete_confirmcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.TextField(),
        ),
    ]
