# Generated by Django 3.2.15 on 2022-08-30 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_auto_20220830_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='current_balance',
            field=models.BigIntegerField(default='0', verbose_name='موجودی حساب'),
        ),
    ]
