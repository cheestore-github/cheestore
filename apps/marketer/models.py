from xml.dom.minidom import Notation
from django.db import models
from accounts.models import CustomUser


class ProfileMrketer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='marketer')
    id_number = models.IntegerField(verbose_name='شماره شناسنامه', max_length=10, unique=True)
    Nationality = models.CharField(verbose_name='ملیت', max_length=64, null=True, blank=True)
    Religion = models.CharField(verbose_name='مذهب', max_length=64, null=True, blank=True)
    father_name = models.CharField(verbose_name='نام پدر',max_length=64, null=True, blank=True)
    address = models.CharField
     
