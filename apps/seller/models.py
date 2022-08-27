from django.db import models
from apps.accounts.models import CustomUser

gender_choices=(('مرد','مرد'),('زن','زن'))


class SellerUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, unique=True)

    gender=models.CharField(verbose_name ='جنسیت', choices = gender_choices, max_length=50,null=True, blank=True)
    birthdate=models.DateField(verbose_name ='تاریخ تولد', max_length=50,null=True, blank=True)
    address=models.TextField(verbose_name ='آدرس', max_length=50,null=True, blank=True)


    def __str__(self):
        return self.user.name + " "+ self.user.family