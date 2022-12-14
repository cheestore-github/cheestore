# Generated by Django 3.2.15 on 2022-08-29 05:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=100, verbose_name='موجودی حساب')),
                ('account_name', models.CharField(max_length=250, verbose_name='صاحب حساب')),
                ('account_number', models.CharField(max_length=100, verbose_name='شماره حساب')),
                ('bank', models.CharField(max_length=100, verbose_name='نام بانک')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WalletTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=250, verbose_name='شماره تراکنش')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('success', 'Success'), ('fail', 'Fail')], default='pending', max_length=200, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=100, verbose_name='مبلغ تراکنش')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, max_length=200, verbose_name='زمان تراکنش')),
                ('wallet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wallet.wallet')),
            ],
        ),
    ]
