from asyncio import BaseEventLoop
from operator import mod
from time import timezone
from unicodedata import category
from django.db import models
from apps.accounts.models import CustomUser

class AgentUser(models.Model):
    
    F_W_US = [
        ('google','جستجو در اینترنت'),
        ('instagram','اینستاگرام'),
        ('telegram','تلگرام'),
        ('friends','دوستان و آشنایان'),
        ('others','سایر')
    ]
    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, unique=True)
    phone=models.CharField(verbose_name ='تلفن ثابت', max_length=50)
    birth_year=models.CharField(verbose_name ='سال تولد', max_length=50)
    residence_city=models.CharField(verbose_name ='شهر محل سکونت', max_length=50)
    agency_city=models.CharField(verbose_name='شهر مورد تقاضا برای نمایندگی', max_length=50)
    job_history=models.TextField(verbose_name='سوابق شغلی')
    last_collab=models.CharField(verbose_name='مدت زمان همکاری در آخرین تجربه شغلی', max_length=50)
    schooling=models.CharField(verbose_name='میزان تحصیلات', max_length=50)
    social_media_skills=models.TextField(verbose_name='مهارت های فضای مجازی', max_length=50)
    job_space=models.TextField(verbose_name='متراژ و نوع مالکیت فضای کار', max_length=50)
    reagent=models.CharField(verbose_name='معرف', max_length=50)
    familiarity_with_us=models.CharField(verbose_name='از چه طریق با مجموعه ما آشنا شدید؟', choices=F_W_US, max_length=50)
    plunge_case=models.CharField(verbose_name='وضعیت اشتغال', max_length=50)
    profational_skills=models.TextField(verbose_name='مهارت های حرفه ای', max_length=50)
    languages=models.TextField(verbose_name='میزان آشنایی شما با زبان انگلیسی یا سایر زبان ها', max_length=50)
    favorites=models.TextField(verbose_name='مزایای شغلی موردعلاقه', max_length=50)
    cv=models.FileField(verbose_name='آپلود فایل رزومه', upload_to='agent_cv/')

    def __str__(self):
        return self.user.name + " "+ self.user.family
    
    class Meta:
        db_table = 'agent'
    
class Rule(models.Model):
    user = models.OneToOneField(CustomUser, verbose_name='نام کاربر', on_delete=models.CASCADE, related_name='ruletocustomuser')
    rule_accept=models.BooleanField(null=True, blank=True)
    rule_deny=models.BooleanField(null=True, blank=True)
    later_read=models.BooleanField(null=True, blank=True)
    
    def __str__(self):
        return self.user.name + " " + self.user.family  
    
    class Meta:
        db_table = 'rule'  
        
class Transfer(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='کاربر', on_delete=models.CASCADE, related_name='bankinfotocustomuser')
    tracking_code = models.CharField(verbose_name='کد ردیابی تراکنش', max_length=50)
    
    def __str__(self):
        return self.user.name + " " + self.user.family
    
    class Meta:
        db_table = 'transfer'
 