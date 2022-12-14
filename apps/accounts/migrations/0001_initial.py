# Generated by Django 3.2.15 on 2022-08-25 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('phone_number', models.CharField(max_length=255, unique=True, verbose_name='تلفن همراه')),
                ('name', models.CharField(blank=True, max_length=150, null=True, verbose_name='نام')),
                ('family', models.CharField(blank=True, max_length=255, null=True, verbose_name='نام خانوادگی')),
                ('national_code', models.CharField(max_length=255, unique=True, verbose_name='کدملی')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='آدرس ایمیل')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
