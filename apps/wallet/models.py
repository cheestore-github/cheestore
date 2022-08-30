from django.db import models
from django.db import IntegrityError
from apps.accounts.models import CustomUser
import uuid


class InsufficientBalance(IntegrityError):
    pass

class Wallet(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(CustomUser, on_delete=models.SET_NULL, null=True)
    current_balance = models.BigIntegerField(verbose_name ="موجودی حساب",default='0')
    account_name = models.CharField(verbose_name ="صاحب حساب", max_length=250)
    account_number = models.CharField(verbose_name ="شماره حساب", max_length=100)
    bank = models.CharField(verbose_name ="نام بانک", max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

    def deposit(self, value):
        self.transaction_set.create(
            value=value,
            running_balance=self.current_balance + value
        )
        self.current_balance += value
        self.save()

    def withdraw(self, value):
        if value > self.current_balance:
            raise InsufficientBalance('This wallet has insufficient balance.')

        self.transaction_set.create(
            value=-value,
            running_balance=self.current_balance - value
        )
        self.current_balance -= value
        self.save()


    class Meta:
        verbose_name = 'کیف پول'
        verbose_name_plural = 'کیف پول ها'

#==================================WalletTransaction=============================================================


status_choices=(('موفق','موفق'),('ناموفق','ناموفق'),('در انتظار پاسخ ','در انتظار پاسخ'))

class Transaction(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.SET_NULL,null=True)
    title=models.CharField(verbose_name='عنوان تراکنش',max_length=200)
    transaction_id = models.UUIDField(verbose_name='شماره تراکنش',primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(verbose_name='وضعیت تراکنش',max_length=200, blank=True,choices=status_choices,default='')    
    value = models.BigIntegerField(verbose_name='مبلغ تراکنش',default=0)
    created_at = models.DateTimeField(verbose_name='تاریخ و زمان تراکنش', max_length=200,auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تراکنش'
        verbose_name_plural = 'تراکنش ها'
    
