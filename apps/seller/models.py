from django.db import models
from apps.accounts.models import CustomUser

gender_choices=(('مرد','مرد'),('زن','زن'))

def upload_profile_image_path(instance, filename):
	    return f'images/sellers/{instance.user.phone_number}/profile/{filename}' 

def upload_document_image_path(instance, filename):
	    return f'images/sellers/{instance.user.phone_number}/documents/{filename}' 

class SellerUser(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, unique=True)
    img_profile = models.ImageField(verbose_name ='عکس پروفایل',upload_to=upload_profile_image_path, default='default_profile_pic.jpg')
    gender=models.CharField(verbose_name ='جنسیت', choices = gender_choices, max_length=10)
    birthdate=models.DateField(verbose_name ='تاریخ تولد', max_length=50,null=True, blank=True)
    img_national_card = models.ImageField(verbose_name ='تصویر کارت ملی',upload_to=upload_document_image_path, default='', blank=True)
    address=models.TextField(verbose_name ='آدرس', max_length=50,null=True, blank=True)


    def __str__(self):
        return self.user.name + " "+ self.user.family