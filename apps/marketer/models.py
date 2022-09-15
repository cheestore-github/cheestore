from xml.dom.minidom import Notation
from django.db import models
from accounts.models import CustomUser



gender_choices=(('M','مرد'),('F','زن'))


class ProfileMrketer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='marketer')
    password= models.CharField(max_length=32, blank=True, null=True)
    birthdate = models.DateTimeField(verbose_name='تولد', blank=True, null=True)
    geder = models.CharField(verbose_name='جنسیت', choices = gender_choices, max_length=8, blank=True, null=True)
    id_number = models.IntegerField(verbose_name='شماره شناسنامه', max_length=10, unique=True)
    Nationality = models.CharField(verbose_name='ملیت', max_length=64, null=True, blank=True)
    Religion = models.CharField(verbose_name='مذهب', max_length=64, null=True, blank=True)
    father_name = models.CharField(verbose_name='نام پدر',max_length=64, null=True, blank=True)
    city = models.CharField(verbose_name='شهر', max_length=64, null=True, blank=True)
    address = models.CharField(verbose_name='ادرس محل سکونت', max_length=512, null=True, blank=True)
    zip_code= models.IntegerField(verbose_name='کدپستی', max_length=10, null=True, blank=False, default='')
    representative = models.CharField(verbose_name='معرف', max_length=256, null=True, blank=True) # 3 peaple and their phone number
    cv = models.FileField(verbose_name='آپلود رزومه',upload_to='resume/', null=True, blank=True)
    personal_image= models.ImageField(verbose_name='عکس پرسنلی',upload_to='upload_document_image_path', null=True, blank=True)
    work_experience = models.CharField(verbose_name='سوابق شغلی', max_length=256, null=True, blank=True)
    Familiarity_socialmedia = models.CharField(verbose_name='میزان آشنایی با فضای مجازی ', max_length=512, null=True, blank=True)   
    Familiarity_Language = models.CharField(verbose_name='آشنایی با زبان خارجی', max_length=512, null=True, blank=True)
    Familiarity_Marketing = models.CharField(verbose_name='آشنایی با متد های روز تبلیغات و بازاریابی', max_length=512 , null=True, blank=True)
    Familiarity_IT = models.CharField(verbose_name='میزان آشنایی با کامپیوتر', max_length=256, null=True, blank=True)   
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.address
    
    class Meta:
        verbose_name = 'نماینده'
        verbose_name_plural = 'نماینده ها '






       

     
