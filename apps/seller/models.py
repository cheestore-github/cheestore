from asyncio import BaseEventLoop
from operator import mod
from time import timezone
from unicodedata import category
from django.db import models
from apps.accounts.models import CustomUser

gender_choices=(('مرد','مرد'),('زن','زن'))


class SellerUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, unique=True, related_name='sellertocustom')

    gender=models.CharField(verbose_name ='جنسیت', choices = gender_choices, max_length=50,null=True, blank=True)
    birthdate=models.DateField(verbose_name ='تاریخ تولد', max_length=50,null=True, blank=True)
    address=models.TextField(verbose_name ='آدرس', max_length=50,null=True, blank=True)


    def __str__(self):
        return self.user.name + " "+ self.user.family
    
#----------------------------------------EccoInfoSellerModel--------------------------
class EccoInformation(models.Model):
    TYPES_OF_WEAR = [
        ('پوشاک','البسه و پوشاک'),
        ('خیاطی','چرخ خیاطی و ملزومات آن'),
        ('کفش','کفش')
    ]
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, unique=True, related_name='eccotocustom')
    
    brand_name = models.CharField(verbose_name='نام برند', max_length=100)
    #owner = models.ForeignKey("SellerUser", verbose_name='صاحب برند', on_delete=models.CASCADE, related_name='eccoinformation')
    owner = models.CharField(verbose_name='صاحب برند', max_length=50, null=True, blank=True)
    category = models.CharField(verbose_name='نوع کالا', max_length=50,choices=TYPES_OF_WEAR)
    sheba_number = models.CharField(verbose_name='شماره شبا', max_length=50, null=True, blank=True)
    description = models.TextField(verbose_name='توضیحات', null=True, blank=True)
    lawful_candid_name = models.CharField(verbose_name='نام و نام خانوادگی نماینده قانونی', max_length=50, null=True, blank=True)
    lawful_candid_nationalcode = models.CharField(verbose_name='کد ملی نماینده قانونی', max_length=10, null=True, blank=True)
    lawful_candid_phone = models.CharField(verbose_name='شماره تماس نماینده قانونی', max_length=11, null=True, blank=True)
    lawful_candid_image = models.ImageField(verbose_name='آپلود عکس کارت ملی', upload_to=None, height_field=None, width_field=None, max_length=None, null=True, blank=True)
    certificate_image = models.ImageField(verbose_name='آپلود تصویر گواهینامه ثبت علامت تجاری', upload_to='comm_sign/')
    logo_image = models.ImageField(verbose_name='آپلود تصویر لوگو', upload_to='favicon/')
    
    def __str__(self):
        return f"{self.brand_name} {self.owner}"
    
#----------------------------------------------------CategoryGender----------------------------------------------------------------
class CategoryGender(models.Model):
    gender = models.CharField(verbose_name='عنوان دسته', max_length=50)  
    published_at = models.DateTimeField(verbose_name='زمان انتشار', auto_now=False, auto_now_add=True)  
    
    def __str__(self):
        return self.gender
    
#----------------------------------------------------CategoryWear----------------------------------------------------------------
class CategoryWear(models.Model):
    wear = models.CharField(verbose_name='عنوان دسته', max_length=50)
    gender = models.ManyToManyField(CategoryGender, verbose_name='جنسیت', related_name='weartogender')
    published_at = models.DateTimeField(verbose_name='زمان انتشار', auto_now=False, auto_now_add=True)  
    
    def __str__(self):
        return self.wear
    
#----------------------------------------------------CategoryTypes----------------------------------------------------------------
class CategoryTypes(models.Model):
    types = models.CharField(verbose_name='عنوان دسته', max_length=50)  
    gender = models.ManyToManyField(CategoryGender, verbose_name='جنسیت', related_name='typestogender')
    wear = models.ForeignKey(CategoryWear, verbose_name='پوشاک', on_delete=models.CASCADE, related_name='typestowear')
    published_at = models.DateTimeField(verbose_name='زمان انتشار', auto_now=False, auto_now_add=True)  
    
    def __str__(self):
        return self.types
    
#----------------------------------------------------FinalCategory----------------------------------------------------------------
class FinalCategory(models.Model):
    title = models.CharField(verbose_name='عنوان دسته', max_length=50)  
    gender = models.ManyToManyField(CategoryGender, verbose_name='جنسیت', related_name='finaltogender')
    wear = models.ForeignKey(CategoryWear, verbose_name='پوشاک', on_delete=models.CASCADE, related_name='finaltowear')
    types = models.ForeignKey(CategoryTypes, verbose_name='انواع', on_delete=models.CASCADE, related_name='finaltotypes')
    published_at = models.DateTimeField(verbose_name='زمان انتشار', auto_now=False, auto_now_add=True)  
    
    def __str__(self):
        return self.title 
    
#------------------------------------------------------------Tag---------------------------------------------------------------
class Tag(models.Model):
    title = models.CharField(verbose_name='تگ ها', max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(verbose_name='زمان ایجاد', auto_now=False, auto_now_add=True)
        
    def __str__(self):
        return self.title
    
#------------------------------------------------------------color--------------------------------------------------------------
class Color(models.Model):
    title = models.CharField(verbose_name='رنگ ها', max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(verbose_name='زمان ایجاد', auto_now=False, auto_now_add=True)
       
    def __str__(self):
        return self.title
    
#------------------------------------------------------------nature--------------------------------------------------------------
class Nature(models.Model):
    title = models.CharField(verbose_name='جنس', max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(verbose_name='زمان ایجاد', auto_now=False, auto_now_add=True)
        
    def __str__(self):
        return self.title
    
#-----------------------------------------------------ProductionModel------------------------------------------------------
# class Production(models.Model):
    
#     CATE = [
#         ('البسه و پوشاک','البسه و پوشاک'),
#         ('تجهیزات دوخت','تجهیزات دوخت'),
#         ('ماشین آلات','ماشین آلات')
#     ]
    
#     name = models.CharField(verbose_name='نام محصول', max_length=50)
#     user = models.ForeignKey(CustomUser, verbose_name='تولید کننده', on_delete=models.CASCADE, related_name='productiontocustomuser')
#     first_category = models.CharField(verbose_name='دسته بندی', max_length=50, choices=CATE, null=True, blank=True)
#     price = models.CharField(verbose_name='قیمت', max_length=50)
#     tags = models.ManyToManyField(Tag, verbose_name='تگ ها', related_name='productiontotag')
#     description = models.TextField(verbose_name='توضیحات', null=True, blank=True)
#     image = models.ImageField(verbose_name='تصویر کالا', upload_to='pro_img/', null=True, blank=True)
#     videofile= models.FileField(upload_to='pro_video/', verbose_name="ویدئو از کالا", null=True, blank=True)
#     stock = models.CharField(verbose_name='موجودی کالا', max_length=50, default=0)
    
#     def __str__(self):
#         return self.name
    
#---------------------------------------------------------ClothesModel---------------------------------------------------------

class Dress(models.Model):
        
    SIZE = [
        ('S','Small'),
        ('M','Medium'),
        ('L','Large'),
        ('XL','XLarge'),
        ('XXL','XXLarge'),
        ('XXXL','XXXLarge')
    ]
    
    SLEEVE = [
        ('آستین آرنج وصله‌دار','آستین آرنج وصله‌دار'),
        ('آستین آویخته','آستین آویخته'),
        ('آستین اپل‌دار','آستین اپل‌دار'),
        ('آستین بدون سرشانه','آستین بدون سرشانه'),
        ('آستین پروانه‌ای','آستین پروانه‌ای'),
        ('آستین خفاشی بلند','آستین خفاشی بلند'),
        ('آستین ژولیت','آستین ژولیت'),
        ('آستین سه‌ربع یا النگویی','آستین سه‌ربع یا النگویی'),
        ('آستین فانوسی','آستین فانوسی'),
        ('آستین گلبرگی (لاله‌ای)','آستین گلبرگی (لاله‌ای)'),
        ('استین بلند','استین بلند'),
        ('استین کوتاه','استین کوتاه'),
        ('بدون استین','بدون استین')        
    ]
    CLOSE_WAY = [
        ('بند','بند'),
        ('دکمه','دکمه'),
        ('زیپ','زیپ'),
        ('زیپ دکمه','زیپ دکمه'),
        ('کش','کش'),
        ('گیره','گیره'),
    ]
    
    COLORS_NUM = [
        ('تک رنگ','تک رنگ'),
        ('2 رنگ','2 رنگ'),
        ('3 رنگ','3 رنگ'),
        ('4 رنگ','4 رنگ'),
        ('5 رنگ','5 رنگ'),
        ('6 رنگ','6 رنگ'),
        ('7 رنگ','7 رنگ'),
        ('8 رنگ','8 رنگ'),
        ('9 رنگ','9 رنگ'),
        ('10 رنگ','10 رنگ'),
        ('11 رنگ','11 رنگ'),
        ('12 رنگ','12 رنگ'),
        ('13 رنگ','13 رنگ'),
        ('14 رنگ','14 رنگ'),
        ('15 رنگ','15 رنگ'),
        ('16 رنگ','16 رنگ'),
        ('17 رنگ','17 رنگ'),
        ('18 رنگ','18 رنگ'),
        ('19 رنگ','19 رنگ'),
        ('20 رنگ','20 رنگ'),
        ('21 رنگ','21 رنگ'),
        ('22 رنگ','22 رنگ'),
        ('23 رنگ','23 رنگ'),
        ('24 رنگ','24 رنگ'),
        ('24 رنگ و بیشتر','24 رنگ و بیشتر')
    ]
    CROTCH = [
        ('فاق بلند','فاق بلند'),
        ('فاق کوتاه','فاق کوتاه'),
        ('فاق متوسط','فاق متوسط')
    ]
    SALE_WAY = [
        ('به صورت سری رنگ','به صورت سری رنگ'),
        ('به صورت سری رنگ با تعداد سایز بندی','به صورت سری رنگ با تعداد سایز بندی')
    ]
    WARRANTY = [
        ('توسط کارخانه','توسط کارخانه'),
        ('دارد','دارد'),
        ('ندارد','ندارد')
    ]
    POCKET = [
        ('دارد','دارد'),
        ('تک جیب','تک جیب'),
        ('دو جیب','دو جیب'),
        ('چهار جیب','چهار جیب'),
        ('چهار جیب','چهار جیب'),
        ('شش جیب','شش جیب'),
        ('هشت جیب و بیشتر','هشت جیب و بیشتر'),
        ('ندارد','ندارد'),
    ]
    HAT = [
        ('دارد','دارد'),
        ('ندارد','ندارد')   
    ]
    # BELT = [
        
    # ]
    WASHING_POINT = [
        ('ابریشم:پارچه پیچانده یا فشرده نشود','ابریشم:پارچه پیچانده یا فشرده نشود'),
        ('پارچه پنبه:پارچه پیچانده یا فشرده نشود','پارچه پنبه:پارچه پیچانده یا فشرده نشود'),
        ('به صورت مجزا شسته شوند.','به صورت مجزا شسته شوند.'),
        ('پارچه نایلون:پارچه نباید زیر تابش مستقیم خورشید خشک گردد','پارچه نایلون:پارچه نباید زیر تابش مستقیم خورشید خشک گردد'),
        ('پارچه پیچانده یا فشرده نشود','پارچه پیچانده یا فشرده نشود'),
        ('چاندری (Chanderi), چیفون (Chiffon):خشک کردن در هوای باز نسبت به خشک کردن زیر نور خورشید برای این پارچه ترجیح داده می شود., در آب سرد با مواد شوینده ملایم باید مورد شستشو قرار گیرد., در دمای کم باید اتو شوند.',
         'چاندری (Chanderi), چیفون (Chiffon):خشک کردن در هوای باز نسبت به خشک کردن زیر نور خورشید برای این پارچه ترجیح داده می شود., در آب سرد با مواد شوینده ملایم باید مورد شستشو قرار گیرد., در دمای کم باید اتو شوند.'),
        ('ریون (Rayon), ژرژت (Georgette), ساتن:شستشو با اب سرد, شستشو به وسیله ماشین توصیه نمی شود, شستشوی خانگی, شستشوی دستی','ریون (Rayon), ژرژت (Georgette), ساتن:شستشو با اب سرد, شستشو به وسیله ماشین توصیه نمی شود, شستشوی خانگی, شستشوی دستی'),
        ('کرپ (Crepe), کوتا دوریا (Kota Doria), لیزی بیزی (Lizzy Bizzy), لینن (Linen), مودال ساتن (Modal Satin), موسلین (Muslin):شستوشو با آب گرم, شستوشو با ماشین, فقط به صورت خشک شسته شود و حتی شستشوی معمولی هم می تواند به پارچه آسیب بزند',
         'کرپ (Crepe), کوتا دوریا (Kota Doria), لیزی بیزی (Lizzy Bizzy), لینن (Linen), مودال ساتن (Modal Satin), موسلین (Muslin):شستوشو با آب گرم, شستوشو با ماشین, فقط به صورت خشک شسته شود و حتی شستشوی معمولی هم می تواند به پارچه آسیب بزند'),
    ]
    STYLE = [
        ('اسپرت','اسپرت'),
        ('رسمی','رسمی'),
        ('روزمره','روزمره'),
        ('کلاسیک','کلاسیک'),
        ('مجلسی','مجلسی')
        
    ]
    DESIGN = [
        ('تارتان (پارچه اسکاتلندی)','تارتان (پارچه اسکاتلندی)'),
        ('چریکی-جنگلی','چریکی-جنگلی'),
        ('چهارخانه','چهارخانه'),
        ('خال‌خالی','خال‌خالی'),
        ('خطوط شکسته','خطوط شکسته'),
        ('خطوط مایل','خطوط مایل'),
        ('راه‌ راه','راه‌ راه'),
        ('ساده','ساده'),
        ('طرح ارتشی','طرح ارتشی'),
        ('طرح بته‌ جقه','طرح بته‌ جقه'),
        ('طرح نوشته','طرح نوشته'),
        ('کارتونی','کارتونی'),
        ('گل‌گلی','گل‌گلی'),
        ('گلدار','گلدار'),
        ('نقش و نگار‌دار','نقش و نگار‌دار'),
        ('طرحدار','طرحدار')  
    ]
    SPATIAL_FEATURE = [
 
    ]
    COLLAR = [
        ('دیپلمات','دیپلمات'),
        ('گرد','گرد'),
        ('یقه آرشال','یقه آرشال'),
        ('یقه اسکی','یقه اسکی'),
        ('یقه انگلیسی','یقه انگلیسی'),
        ('یقه ایرانی','یقه ایرانی'),
        ('یقه ب.ب','یقه ب.ب'),
        ('یقه بلیزری','یقه بلیزری'),
        ('یقه چهارگوش (خشتی)','یقه چهارگوش (خشتی)'),
        ('یقه چینی','یقه چینی'),
        ('یقه دراپه','یقه دراپه'),
        ('یقه شکاری','یقه شکاری'),
        ('یقه شومیزی','یقه شومیزی'),
        ('یقه فانتزی','یقه فانتزی'),
        ('یقه فرنچی','یقه فرنچی'),
        ('یقه قایقی (بلمی، کشتی)','یقه قایقی (بلمی، کشتی)'),
        ('یقه لباس ایستاده','یقه لباس ایستاده'),
        ('یقه ملوانی','یقه ملوانی'),
        ('یقه هفت','یقه هفت'),
        ('یقه ساده','یقه ساده'),  
    ]
        
    CATE = [
        ('البسه و پوشاک','البسه و پوشاک'),
        ('تجهیزات دوخت','تجهیزات دوخت'),
        ('ماشین آلات','ماشین آلات')
    ]
    
    name = models.CharField(verbose_name='نام محصول', max_length=50)
    user = models.ForeignKey(CustomUser, verbose_name='تولید کننده', on_delete=models.CASCADE, related_name='dresstocustomuser')
    first_category = models.CharField(verbose_name='دسته بندی', max_length=50, choices=CATE, null=True, blank=True)
    price = models.CharField(verbose_name='قیمت', max_length=50)
    tags = models.ManyToManyField(Tag, verbose_name='تگ ها', related_name='dresstotag')
    description = models.TextField(verbose_name='توضیحات', null=True, blank=True)
    image = models.ImageField(verbose_name='تصویر کالا', upload_to='pro_img/', null=True, blank=True)
    videofile= models.FileField(upload_to='pro_video/', verbose_name="ویدئو از کالا", null=True, blank=True)
    
    # production = models.OneToOneField(Production, verbose_name='محصول', on_delete=models.CASCADE, related_name='dresstoproduction',null=True,blank=True)
    genders = models.ForeignKey(CategoryGender, verbose_name='جنسیت', on_delete=models.CASCADE, related_name='dresstogender')
    wears = models.ForeignKey(CategoryWear, verbose_name='نوع پوشیدنی', on_delete=models.CASCADE, related_name='dresstowear')
    types = models.ForeignKey(CategoryTypes, verbose_name='نام پوشیدنی', on_delete=models.CASCADE, related_name='dersstotypes')
    size = models.CharField(verbose_name='سایز', max_length=50, choices=SIZE)
    numbers = models.IntegerField(verbose_name='تعداد')
    nature = models.ForeignKey(Nature, verbose_name='جنس', on_delete=models.CASCADE, related_name='dresstonature')
    colors = models.ManyToManyField(Color, verbose_name='رنگبندی', related_name='dresstocolor')
    sleeve = models.CharField(verbose_name='نوع آستین', max_length=100, choices=SLEEVE)
    close_way = models.CharField(verbose_name='نحوه بسته شدن', max_length=100, choices=CLOSE_WAY)
    colors_num = models.CharField(verbose_name='تعداد رنگبندی', max_length=100, choices=COLORS_NUM)
    crotch = models.CharField(verbose_name='نوع فاق', max_length=100, choices=CROTCH)
    sale_way = models.CharField(verbose_name='نحوه فروش', max_length=100, choices=SALE_WAY)
    warranty = models.CharField(verbose_name='گارانتی', max_length=100, choices=WARRANTY)
    pocket = models.CharField(verbose_name='جیب', max_length=100, choices=POCKET)
    hat = models.CharField(verbose_name='کلاه', max_length=100, choices=HAT)
    # Belt = models.CharField(verbose_name='کمربند', max_length=50, choices=BELT)
    washing_point = models.CharField(verbose_name='نکات شستشو', max_length=500, choices=WASHING_POINT)
    style = models.CharField(verbose_name='استایل', max_length=100, choices=STYLE)
    design = models.CharField(verbose_name='طرح', max_length=100, choices=DESIGN)
    spatial_feature = models.CharField(verbose_name='ویژگی های تخصصی', max_length=100, choices=SPATIAL_FEATURE)
    collar = models.CharField(verbose_name='یقه', max_length=100, choices=COLLAR)
    
    def __str__(self):
        return self.name
    
#---------------------------------------------------------SewingEquipment------------------------------------------------------

class Equipment(models.Model):
    WEIDTH = [
        ('بر حسب متر','بر حسب متر'),
        ('بر حسب یارد','بر حسب یارد') 
    ]
    COLORS_NUM = [
        ('تک رنگ','تک رنگ'),
        ('2 رنگ','2 رنگ'),
        ('3 رنگ','3 رنگ'),
        ('4 رنگ','4 رنگ'),
        ('5 رنگ','5 رنگ'),
        ('6 رنگ','6 رنگ'),
        ('7 رنگ','7 رنگ'),
        ('8 رنگ','8 رنگ'),
        ('9 رنگ','9 رنگ'),
        ('10 رنگ','10 رنگ'),
        ('11 رنگ','11 رنگ'),
        ('12 رنگ','12 رنگ'),
        ('13 رنگ','13 رنگ'),
        ('14 رنگ','14 رنگ'),
        ('15 رنگ','15 رنگ'),
        ('16 رنگ','16 رنگ'),
        ('17 رنگ','17 رنگ'),
        ('18 رنگ','18 رنگ'),
        ('19 رنگ','19 رنگ'),
        ('20 رنگ','20 رنگ'),
        ('21 رنگ','21 رنگ'),
        ('22 رنگ','22 رنگ'),
        ('23 رنگ','23 رنگ'),
        ('24 رنگ','24 رنگ'),
        ('24 رنگ و بیشتر','24 رنگ و بیشتر')
    ]
    SALE_WAY = [
        ('به صورت طاقه تک','به صورت طاقه تک'),
        ('به صورت عدلی','به صورت عدلی')
    ]
    WARRANTY = [
        ('توسط کارخانه','توسط کارخانه'),
        ('دارد','دارد'),
        ('ندارد','ندارد')
    ]
    USING = [
        ('البسه','البسه'),
        ('تزیینی','تزیینی'),
        ('مبلمان','مبلمان')
    ]
    WASHING_POINT = [
        ('ابریشم:پارچه پیچانده یا فشرده نشود','ابریشم:پارچه پیچانده یا فشرده نشود'),
        ('پارچه پنبه:پارچه پیچانده یا فشرده نشود','پارچه پنبه:پارچه پیچانده یا فشرده نشود'),
        ('به صورت مجزا شسته شوند.','به صورت مجزا شسته شوند.'),
        ('پارچه نایلون:پارچه نباید زیر تابش مستقیم خورشید خشک گردد','پارچه نایلون:پارچه نباید زیر تابش مستقیم خورشید خشک گردد'),
        ('پارچه پیچانده یا فشرده نشود','پارچه پیچانده یا فشرده نشود'),
        ('چاندری (Chanderi), چیفون (Chiffon):خشک کردن در هوای باز نسبت به خشک کردن زیر نور خورشید برای این پارچه ترجیح داده می شود., در آب سرد با مواد شوینده ملایم باید مورد شستشو قرار گیرد., در دمای کم باید اتو شوند.',
         'چاندری (Chanderi), چیفون (Chiffon):خشک کردن در هوای باز نسبت به خشک کردن زیر نور خورشید برای این پارچه ترجیح داده می شود., در آب سرد با مواد شوینده ملایم باید مورد شستشو قرار گیرد., در دمای کم باید اتو شوند.'),
        ('ریون (Rayon), ژرژت (Georgette), ساتن:شستشو با اب سرد, شستشو به وسیله ماشین توصیه نمی شود, شستشوی خانگی, شستشوی دستی','ریون (Rayon), ژرژت (Georgette), ساتن:شستشو با اب سرد, شستشو به وسیله ماشین توصیه نمی شود, شستشوی خانگی, شستشوی دستی'),
        ('کرپ (Crepe), کوتا دوریا (Kota Doria), لیزی بیزی (Lizzy Bizzy), لینن (Linen), مودال ساتن (Modal Satin), موسلین (Muslin):شستوشو با آب گرم, شستوشو با ماشین, فقط به صورت خشک شسته شود و حتی شستشوی معمولی هم می تواند به پارچه آسیب بزند',
         'کرپ (Crepe), کوتا دوریا (Kota Doria), لیزی بیزی (Lizzy Bizzy), لینن (Linen), مودال ساتن (Modal Satin), موسلین (Muslin):شستوشو با آب گرم, شستوشو با ماشین, فقط به صورت خشک شسته شود و حتی شستشوی معمولی هم می تواند به پارچه آسیب بزند'),
    ]
    HEIGHT = [
        ('متر','متر'),
        ('یارد','یارد')        
    ]
    DESIGN = [
        ('تارتان (پارچه اسکاتلندی)','تارتان (پارچه اسکاتلندی)'),
        ('چریکی-جنگلی','چریکی-جنگلی'),
        ('چهارخانه','چهارخانه'),
        ('خال‌خالی','خال‌خالی'),
        ('خطوط شکسته','خطوط شکسته'),
        ('خطوط مایل','خطوط مایل'),
        ('راه‌ راه','راه‌ راه'),
        ('ساده','ساده'),
        ('طرح ارتشی','طرح ارتشی'),
        ('طرح بته‌ جقه','طرح بته‌ جقه'),
        ('طرح نوشته','طرح نوشته'),
        ('کارتونی','کارتونی'),
        ('گل‌گلی','گل‌گلی'),
        ('گلدار','گلدار'),
        ('نقش و نگار‌دار','نقش و نگار‌دار'),
        ('طرحدار','طرحدار')
    ]
    WEIGHT = [
        
    ]
    TISSUE_DENSITY = [
       ('بافت توری','بافت توری'), 
       ('بافت دانه گندمی','بافت دانه گندمی'),
       ('بافت ساتن یا ساتین','بافت ساتن یا ساتین'), 
       ('بافت ساده یا تافته','بافت ساده یا تافته'), 
       ('بافت سرژه','بافت سرژه'), 
       ('بافت کائوچو','بافت کائوچو'), 
       ('بافت کرپ پوری','بافت کرپ پوری'), 
       ('بافت کرپ تاری','بافت کرپ تاری'), 
       ('بافت کرد','بافت کرد'),  
    ]
        
    CATE = [
        ('البسه و پوشاک','البسه و پوشاک'),
        ('تجهیزات دوخت','تجهیزات دوخت'),
        ('ماشین آلات','ماشین آلات')
    ]
    
    name = models.CharField(verbose_name='نام محصول', max_length=50)
    user = models.ForeignKey(CustomUser, verbose_name='تولید کننده', on_delete=models.CASCADE, related_name='equipmenttocustomuser')
    first_category = models.CharField(verbose_name='دسته بندی', max_length=50, choices=CATE, null=True, blank=True)
    price = models.CharField(verbose_name='قیمت', max_length=50)
    tags = models.ManyToManyField(Tag, verbose_name='تگ ها', related_name='equipmenttotag')
    description = models.TextField(verbose_name='توضیحات', null=True, blank=True)
    image = models.ImageField(verbose_name='تصویر کالا', upload_to='pro_img/', null=True, blank=True)
    videofile= models.FileField(upload_to='pro_video/', verbose_name="ویدئو از کالا", null=True, blank=True)

    # production = models.ForeignKey(Production, verbose_name='محصول', on_delete=models.CASCADE, related_name='equipmenttoprduction')
    name = models.CharField(verbose_name='نوع تجهیز', max_length=50)
    weidth = models.CharField(verbose_name='عرض طاقه پارچه', max_length=100, choices=WEIDTH)
    nature = models.ForeignKey(Nature, verbose_name='جنس', on_delete=models.CASCADE, related_name='equipmenttonature')
    colors_num = models.CharField(verbose_name='تعداد رنگبندی', max_length=100, choices=COLORS_NUM)
    colors = models.ManyToManyField(Color, verbose_name='رنگبندی', related_name='equipmenttocolor')
    sale_way = models.CharField(verbose_name='نحوه فروش', max_length=100, choices=SALE_WAY)
    warranty = models.CharField(verbose_name='گارانتی', max_length=100, choices=WARRANTY)
    using = models.CharField(verbose_name='کاربرد پارچه', max_length=100, choices=USING)
    washing_point = models.CharField(verbose_name='نکات شستشو', max_length=500, choices=WASHING_POINT)
    height = models.CharField(verbose_name='طول طاق پارچه', max_length=100, choices=HEIGHT)
    design = models.CharField(verbose_name='طرح', max_length=100, choices=DESIGN)
    weight = models.CharField(verbose_name='وزن پارچه', max_length=100, choices=WEIGHT)
    tissue_density = models.CharField(verbose_name='تراکم بافت', max_length=100, choices=TISSUE_DENSITY)
    
    def __str__(self):
        return self.name
    
#-------------------------------------------------------IndustrialMachinesModel------------------------------------------------

class Machines(models.Model):
    CYLINDER_BED = [
        ('دارد','دارد'),
        ('ندارد','ندارد')
    ]
    FLAT_BED = [
        ('دارد','دارد'),
        ('ندارد','ندارد')
    ]
    SALE_WAY = [
        ('یک دستگاه','یک دستگاه')
    ]
    WARRANTY = [
        ('توسط کارخانه','توسط کارخانه'),
        ('دارد','دارد'),
        ('ندارد','ندارد')
    ]
    GHAB_MAKO = [
        ('کمپلت تمام دورک','کمپلت تمام دورک'),
        ('کمپلت نیم دور','کمپلت نیم دور')
    ]
    GHABELIAT_DOKHT = [
        ('اتوماتیک','اتوماتیک'),
        ('تمام خود کار بدون کاربر','تمام خود کار بدون کاربر'),
        ('دستی','دستی'),
        ('نیمه اتومات','نیمه اتومات')
    ]
    MAKO = [
        ('کمپلت تمام دور(کمپلت صنعتی)','کمپلت تمام دور(کمپلت صنعتی)'),
        ('کمپلت نیم دور','کمپلت نیم دور')
    ]
    MASORE = [
        ('پلاستیکی','پلاستیکی'),
        ('شیشه ایی','شیشه ایی'),
        ('فلزی','فلزی')
    ]
    MASORE_POR = [
        ('دارد','دارد'),
        ('ندارد','ندارد')
    ]
    NAKH = [
        ('ابریشمی با روکش فلزی (گلابتون)','ابریشمی با روکش فلزی (گلابتون)'),
        ('پولیستری','پولیستری'),
        ('ریونی','ریونی'),
        ('عمامه ای (ابریشمی و پنبه ای)','عمامه ای (ابریشمی و پنبه ای)'),
        ('کاموایی','کاموایی'),
        ('کتانی','کتانی'),
        ('کنفی','کنفی'),
        ('کوبلن دوزی و مِز','کوبلن دوزی و مِز'),
        ('لمه','لمه'),
        ('نایلونی','نایلونی'),
        ('نخ ابریشم','نخ ابریشم'),
        ('نخ پشمی','نخ پشمی'),
        ('نخ پنبه','نخ پنبه'),
        ('نخ دکمه','نخ دکمه'),
        ('نخ دمسه','نخ دمسه'),
        ('نخ سر کیسه دوزی','نخ سر کیسه دوزی'),
        ('نخ سردوزی','نخ سردوزی'),
        ('نخ فاستونی','نخ فاستونی'),
        ('نخ فلزی','نخ فلزی'),
        ('نخ قیطان','نخ قیطان'),
        ('نخ گلدوزی','نخ گلدوزی'),
        ('نخ متالیک','نخ متالیک'),
        ('نخ همه منظوره(پولیستر)','نخ همه منظوره(پولیستر)'),
        ('غیره','غیره')
    ]
    PEDAL = [
        ('دارد','دارد'),
        ('ندارد','ندارد')
    ]
    SOZAN_NAKHKON = [
        ('دارد','دارد'),
        ('ندارد','ندارد')
    ]
    TAVAN = [
        ('خانگی','خانگی'),
        ('صنعتی','صنعتی'),
        ('نیمه صنعتی','نیمه صنعتی')
    ]
    MACHIN_WEIGHT = [
        ('کمتر از 5 کیلو گرم','کمتر از 5 کیلو گرم'),
        ('کمتر از 10 کیلوگرم','کمتر از 10 کیلوگرم'),
        ('کمتر از 15 کیلوگرم','کمتر از 15 کیلوگرم'),
        ('کمتر از 20 کیلوگرم','کمتر از 20 کیلوگرم'),
        ('کمتر از 40 کیلوگرم','کمتر از 40 کیلوگرم'),
        ('بیشتر از 40 کیلو گرم زیر 100 کیلوگرم','بیشتر از 40 کیلو گرم زیر 100 کیلوگرم'),
        ('بیشتر از 100 کیلو گرم','بیشتر از 100 کیلو گرم'),
    ]
    TYPE = [
        ('چرخ خیاطی Post-bed','چرخ خیاطی Post-bed'),
        ('چرخ خیاطی با قابلیت گلدوزی','چرخ خیاطی با قابلیت گلدوزی'),
        ('چرخ خیاطی بدون دسته (Off-the-arm)','چرخ خیاطی بدون دسته (Off-the-arm)'),
        ('چرخ خیاطی دارای صفحه کار استوانه‌ای (Cylinder Bed)','چرخ خیاطی دارای صفحه کار استوانه‌ای (Cylinder Bed)'),
        ('چرخ خیاطی دارای صفحه کار تخت (Flat-bed)','چرخ خیاطی دارای صفحه کار تخت (Flat-bed)'),
        ('چرخ خیاطی دستی','چرخ خیاطی دستی'),
        ('چرخ خیاطی دو سوزنه','چرخ خیاطی دو سوزنه'),
        ('چرخ خیاطی سردوز (Overlock)','چرخ خیاطی سردوز (Overlock)'),
        ('چرخ خیاطی قابل حمل','چرخ خیاطی قابل حمل'),
        ('چرخ خیاطی کامپیوتری','چرخ خیاطی کامپیوتری'),
        ('چرخ‌های خیاطی جادکمه زن','چرخ‌های خیاطی جادکمه زن'),   
    ]
        
    CATE = [
        ('البسه و پوشاک','البسه و پوشاک'),
        ('تجهیزات دوخت','تجهیزات دوخت'),
        ('ماشین آلات','ماشین آلات')
    ]
    
    name = models.CharField(verbose_name='نام محصول', max_length=50)
    user = models.ForeignKey(CustomUser, verbose_name='تولید کننده', on_delete=models.CASCADE, related_name='machintocustomuser')
    first_category = models.CharField(verbose_name='دسته بندی', max_length=50, choices=CATE, null=True, blank=True)
    price = models.CharField(verbose_name='قیمت', max_length=50)
    tags = models.ManyToManyField(Tag, verbose_name='تگ ها', related_name='machintotag')
    description = models.TextField(verbose_name='توضیحات', null=True, blank=True)
    image = models.ImageField(verbose_name='تصویر کالا', upload_to='pro_img/', null=True, blank=True)
    videofile= models.FileField(upload_to='pro_video/', verbose_name="ویدئو از کالا", null=True, blank=True)
    
    # production = models.ForeignKey(Production, verbose_name='محصول', on_delete=models.CASCADE, related_name='machintoproduction')
    cylinder_bed = models.CharField(verbose_name='صفحه کار استوانه ای', max_length=100, choices=CYLINDER_BED)
    flat_bed = models.CharField(verbose_name='صفحه کار تخت', max_length=100, choices=FLAT_BED)
    sale_way = models.CharField(verbose_name='نحوه فروش', max_length=100, choices=SALE_WAY)
    warranty = models.CharField(verbose_name='گارانتی', max_length=100, choices=WARRANTY)
    ghab_mako = models.CharField(verbose_name='سیستم قاب ماکو', max_length=100, choices=GHAB_MAKO)
    ghabeliat_dokht = models.CharField(verbose_name='قابلیت دوخت', max_length=50, choices=GHABELIAT_DOKHT)
    mako = models.CharField(verbose_name='ماکو', max_length=100, choices=MAKO)
    masore = models.CharField(verbose_name='ماسوره', max_length=100, choices=MASORE)
    masore_por = models.CharField(verbose_name='ماسوره پر کن', max_length=100, choices=MASORE_POR)
    nakh = models.CharField(verbose_name='نخ مورد استفاده دستگاه', max_length=100, choices=NAKH)
    pedal = models.CharField(verbose_name='پدال', max_length=100, choices=PEDAL)
    sozan_nakhkon = models.CharField(verbose_name='سوزن نخ کن', max_length=100, choices=SOZAN_NAKHKON)
    tavan = models.CharField(verbose_name='توان ساعت و حجم کار دستگاه', max_length=100, choices=TAVAN)
    machin_weight = models.CharField(verbose_name='وزن دستگاه', max_length=100, choices=MACHIN_WEIGHT)
    type = models.CharField(verbose_name='نوع چرخ خیاطی', max_length=100, choices=TYPE)
    
    def __ste__(self):
        return self.name

    
#-----------------------------------------------------------Ticket--------------------------------------------------------------

class Ticket(models.Model):
    title = models.CharField(verbose_name='موضوع تیکت', max_length=30, null=False, blank=False)
    description = models.TextField(verbose_name='توضیحات', null=True, blank=True)
    att_file = models.FileField(verbose_name='فایل الصاق شده', upload_to = "ticket_att/", null=True, blank=True)
    create_date = models.DateTimeField(verbose_name='زمان ایجاد تیکت', auto_now_add=True)
    status = models.BooleanField(verbose_name='وضعیت تیکت', default=True)
    user = models.OneToOneField(CustomUser, on_delete=models.DO_NOTHING, related_name="TickToCustomUser", verbose_name='کاربر', null=True, blank=True)

    class Meta:
        verbose_name="Ticket"
        verbose_name_plural="Tickets"

    def __str__(self) -> str:
        return f"{self.title } - { self.user}"


class TickComment(models.Model):

    user=models.ForeignKey(CustomUser,null=True,on_delete=models.SET_NULL,related_name="CommentToUser",verbose_name="کاربر") 
    admin = models.CharField(verbose_name='پشتیان سایت', max_length=50, null=True, blank=True)  
    ticket=models.ForeignKey(Ticket,on_delete=models.CASCADE,related_name="CommentToTicket",verbose_name='تیکت', null=True, blank=True)
    reply=models.TextField(verbose_name='پاسخ تیکت', null=True, blank=True)
    att_file = models.FileField(verbose_name='فایل الصاق شده', upload_to = "ticket_att/", null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='زمان پاسخگویی', auto_now=False, auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name="TikComment"
        verbose_name_plural="TikComments"

    def __str__(self) -> str:
        return f"{self.ticket} - {self.user}" 