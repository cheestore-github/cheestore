# Generated by Django 3.2.15 on 2022-09-15 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileMrketer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(blank=True, max_length=32, null=True)),
                ('birthdate', models.DateTimeField(blank=True, null=True, verbose_name='تولد')),
                ('geder', models.CharField(blank=True, choices=[('M', 'مرد'), ('F', 'زن')], max_length=8, null=True, verbose_name='جنسیت')),
                ('id_number', models.IntegerField(max_length=10, unique=True, verbose_name='شماره شناسنامه')),
                ('Nationality', models.CharField(blank=True, max_length=64, null=True, verbose_name='ملیت')),
                ('Religion', models.CharField(blank=True, max_length=64, null=True, verbose_name='مذهب')),
                ('father_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='نام پدر')),
                ('city', models.CharField(blank=True, max_length=64, null=True, verbose_name='شهر')),
                ('address', models.CharField(blank=True, max_length=512, null=True, verbose_name='ادرس محل سکونت')),
                ('zip_code', models.IntegerField(default='', max_length=10, null=True, verbose_name='کدپستی')),
                ('representative', models.CharField(blank=True, max_length=256, null=True, verbose_name='معرف')),
                ('cv', models.FileField(blank=True, null=True, upload_to='resume/', verbose_name='آپلود رزومه')),
                ('personal_image', models.ImageField(blank=True, null=True, upload_to='upload_document_image_path', verbose_name='عکس پرسنلی')),
                ('work_experience', models.CharField(blank=True, max_length=256, null=True, verbose_name='سوابق شغلی')),
                ('Familiarity_socialmedia', models.CharField(blank=True, max_length=512, null=True, verbose_name='میزان آشنایی با فضای مجازی ')),
                ('Familiarity_Language', models.CharField(blank=True, max_length=512, null=True, verbose_name='آشنایی با زبان خارجی')),
                ('Familiarity_Marketing', models.CharField(blank=True, max_length=512, null=True, verbose_name='آشنایی با متد های روز تبلیغات و بازاریابی')),
                ('Familiarity_IT', models.CharField(blank=True, max_length=256, null=True, verbose_name='میزان آشنایی با کامپیوتر')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='marketer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'نماینده',
                'verbose_name_plural': 'نماینده ها ',
            },
        ),
    ]