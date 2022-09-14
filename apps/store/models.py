from django.db import models
from accounts.models import CustomUser
   

gender_choices=(('مرد','مرد'),('زن','زن'))

def upload_profile_image_path(instance, filename):
	    return f'images/sellers/{instance.user.phone_number}/profile/{filename}' 

def upload_document_image_path(instance, filename):
	    return f'images/sellers/{instance.user.phone_number}/documents/{filename}'  


class Store(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='user_store')
    province = models.CharField(verbose_name='استان', max_length=50)
    city = models.CharField(verbose_name='شهر',max_length=50)
    address = models.CharField(verbose_name='آدرس ',max_length=255)
    telephone_number = models.CharField(verbose_name='تلفن ثابت', max_length=11, null=True, blank=True)
    square_meter = models.FloatField(verbose_name='متراژ')
    zip_code = models.CharField(verbose_name='کد پستی', max_length=10)
    is_active = models.BooleanField(default=True)
    img_profile = models.ImageField(verbose_name ='عکس پروفایل',upload_to=upload_profile_image_path, default='default_profile_pic.jpg')
    gender=models.CharField(verbose_name ='جنسیت', choices = gender_choices, max_length=10)
    img_national_card = models.ImageField(verbose_name ='تصویر کارت ملی',upload_to=upload_document_image_path, default='', blank=True)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'مغازه'
        verbose_name_plural = 'مغازه ها ' 

