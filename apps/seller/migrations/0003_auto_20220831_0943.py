# Generated by Django 3.2.15 on 2022-08-31 05:13

import apps.seller.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_auto_20220830_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selleruser',
            name='img_national_card',
            field=models.ImageField(blank=True, default='', upload_to=apps.seller.models.upload_document_image_path, verbose_name='تصویر کارت ملی'),
        ),
        migrations.AlterField(
            model_name='selleruser',
            name='img_profile',
            field=models.ImageField(default='default_profile_pic.jpg', upload_to=apps.seller.models.upload_profile_image_path, verbose_name='عکس پروفایل'),
        ),
    ]