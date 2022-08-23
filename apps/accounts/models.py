from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# class Example(models.Model):
#     category = models.JSONField(verbose_name="مردانه", default ={'men':[{'jorab':['mardane','zanane', 'bachegane']}, 'shalvr']})


class MyUserManager(BaseUserManager):
    def create_user(self, name,family,phone_number,national_code,email, password=None):
        if not phone_number:
            raise ValueError('تلفن همراه باید وارد شود')

        user = self.model(
            name=name,
            family=family,
            phone_number=phone_number,
            national_code= national_code,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name,family,phone_number,national_code,email, password=None):
        user = self.create_user(
            name = name,
            family=family,
            phone_number= phone_number,
            national_code=national_code,
            email=email,
            password=password
            )
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    phone_number = models.CharField(verbose_name='تلفن همراه',max_length=255,unique=True)
    name = models.CharField(verbose_name='نام',max_length=150, null=True, blank=True)
    family = models.CharField(verbose_name='نام خانوادگی',max_length=255,null=True,blank=True)
    national_code = models.CharField(verbose_name='کدملی',max_length=255,unique=True)
    email = models.EmailField(verbose_name='آدرس ایمیل',max_length=255,unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['name','family','national_code','email']

    def __str__(self):
        return f"{self.name} {self.family}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
