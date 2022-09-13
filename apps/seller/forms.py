import re
from django import forms
from .models import EccoInformation, SellerUser, CategoryGender, CategoryWear,CategoryTypes, FinalCategory, Nature, Color, Tag
from apps.accounts.models import CustomUser
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.shortcuts import render, redirect, get_object_or_404


class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='رمز عبور',widget=forms.PasswordInput)
    password2 = forms.CharField(label='تکرار رمز عبور',widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('name', 'family', 'phone_number', 'national_code', 'email', 'password1', 'password2')


    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("رمز عبور مطابقت ندارد")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class SellerRegisterForm(forms.ModelForm):
    birthdate = forms.DateField(label='تاریخ تولد', required=False,
                                widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'تاریخ تولد خود را وارد کنید', 'type':'date'}),
                                error_messages={'required':'این فیلد الزامی است'}
                                )

    class Meta:
        model = SellerUser
        fields = ['gender','birthdate', 'address']

#==================================================================================================================================================

class SellerLoginForm(forms.ModelForm):
    phone_number = forms.CharField(label="تلفن همراه",
                                   widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'شماره تلفن همراه خود را وارد کنید'}),
                                   error_messages={'required':'این فیلد الزامی است'}
                                   )
    password = forms.CharField(label="رمز عبور",
                                   widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'رمز عبور را وارد کنید'}),
                                   error_messages={'required':'این فیلد الزامی است'}
                                   )

    class Meta:
        model = SellerUser
        fields=['phone_number', 'password']


    

#================================================================================================================================


# class PhoneRegisterForm(forms.ModelForm):

#     class Meta:
#         model = SellerUser
#         fields = ('phone_number',)
#         widgets={
#             'phone_number':forms.TextInput(attrs={'placeholder':'تلفن همراه خود را وارد کنید','class':'form-control'})}


class PhoneRegisterForm(forms.Form):
    phone_number = forms.CharField(label="", help_text="مثال: 09123456789",
                                    # widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'شماره تلفن همراه خود را وارد کنید'}),
                                    # error_messages={'required':'این فیلد الزامی است'},
                                    # validators=[RegexValidator(regex='^(09)\d{9}$',message="تلفن همراه می بایست 11رقم و فقط شامل عدد باشد  ",)]
                                    )
    
#------------------------------------RegisterEccoInfoSeller-----------------------

class RegisterEccoInfoUserForm(forms.Form):
    
    TYPES_OF_WEAR = [
        ('پوشاک','البسه و پوشاک'),
        ('خیاطی','چرخ خیاطی و ملزومات آن'),
        ('کفش','کفش')
    ]
    
    brand_name = forms.CharField(label="نام برند",
                                   error_messages={'required':'این فیلد الزامی است'}
                                   )
    owner = forms.CharField(label="نام و نام خانوادگی صاحب برند",
                                   error_messages={'required':'این فیلد الزامی است'}
                                   )
    category = forms.ChoiceField(choices = TYPES_OF_WEAR,
                                 label="نوع کالا",
                                 error_messages={'required':'این فیلد الزامی است'}
                                   )
    sheba_number = forms.CharField(label="شماره شبا",
                                   error_messages={'required':'شماره شبا اشتباه وارد شده است.'}
                                   )
    description = forms.CharField(label="توضیحات",
                                  widget=forms.Textarea,
                                  required = False
                                  )                               
    lawful_candid_name = forms.CharField(label="نام و نام خانوادگی نماینده قانونی",
                                   required = False
                                   )                                   
    lawful_candid_nationalcode = forms.CharField(label="کد ملی نماینده قانونی",
                                   validators=[RegexValidator(message="کد ملی می بایست 10رقم و فقط شامل عدد باشد  ",)],
                                   required = False
                                   )
    lawful_candid_phone = forms.CharField(label="شماره موبایل نماینده قانونی", help_text="مثال: 09123456789",
                                   validators=[RegexValidator(regex='^(09)\d{9}$',message="تلفن همراه می بایست 11رقم و فقط شامل عدد باشد  ",)],
                                   required = False
                                   ) 
    lawful_candid_image = forms.ImageField(label="آپلود تصویر نماینده قانونی",
                                           required = False
                                           )                                   
    certificate_image = forms.ImageField(label="آپلود تصویر گواهینامه ثبت علامت تجاری",
                                         #required = False,
                                         error_messages={'required':'این فیلد الزامی است'}
                                   )
    logo_image = forms.ImageField(label="آپلود تصویر لوگو",
                                  #required = False,
                                  error_messages={'required':'این فیلد الزامی است'}
                                   )
    
#-------------------------------------------------------SelectCategoryProductionForm-----------------------------------------------------
class SelectCategory(forms.Form):
    CATE = [
        ('البسه و پوشاک','البسه و پوشاک'),
        ('تجهیزات دوخت','تجهیزات دوخت'),
        ('ماشین آلات','ماشین آلات')
    ]
    
    first_category = forms.ChoiceField(choices=CATE,
                               label="محصول مورد نظر خود را انتخاب کنید.",
                               error_messages={'required':'این فیلد الزامی است.'}
                               )
    
#---------------------------------------------------------AddProduntionForm----------------------------------------------------------
    
# class AddProductionForm(forms.Form):
    
    # CATE = [
    #     ('البسه و پوشاک','البسه و پوشاک'),
    #     ('تجهیزات دوخت','تجهیزات دوخت'),
    #     ('ماشین آلات','ماشین آلات')
    # ]
    
    # name = forms.CharField(label="نام کالا",
    #                                error_messages={'required':'این فیلد الزامی است'}
    #                                )
    # first_category = forms.ChoiceField(label="دسته بندی محصول",
    #                                    choices=CATE,
    #                                    error_messages={'required':'این فیلد الزامی است'}
    #                                 )
    # price = forms.CharField(label="قیمت",
    #                         error_messages={'required':'این فیلد الزامی است'}
    #                                 )
    # tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),
    #                                        widget=forms.CheckboxSelectMultiple,
    #                                        label="تگ ها",
    #                                        error_messages={'required':'این فیلد الزامی است'}
    #                                 )
    # description = forms.CharField(label="توضیحات",
    #                               widget=forms.Textarea,
    #                               required = False
    #                                 )
    # image = forms.ImageField(label="آپلود تصویر  کالا",
    #                          required = False
    #                                 )
    # videofile = forms.FileField(label="آپلود ویدئوی کالا",
    #                             required = False
    #                                 )
   
#---------------------------------------------------------AddDressForm----------------------------------------------------------
    
class AddDressForm(forms.Form):
   
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
    # 
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
    
   name = forms.CharField(label="نام کالا",
                                   error_messages={'required':'این فیلد الزامی است'}
                                   )
   first_category = forms.ChoiceField(label="دسته بندی محصول",
                                       choices=CATE,
                                       error_messages={'required':'این فیلد الزامی است'}
                                    )
   price = forms.CharField(label="قیمت",
                            error_messages={'required':'این فیلد الزامی است'}
                                    )
   tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),
                                           widget=forms.CheckboxSelectMultiple,
                                           label="تگ ها",
                                           error_messages={'required':'این فیلد الزامی است'}
                                    )
   description = forms.CharField(label="توضیحات",
                                  widget=forms.Textarea,
                                  required = False
                                    )
   image = forms.ImageField(label="آپلود تصویر  کالا",
                             required = False
                                    )
   videofile = forms.FileField(label="آپلود ویدئوی کالا",
                                required = False
                                    )
   genders = forms.ModelChoiceField(queryset=CategoryGender.objects.all(),
                                     label="جنسیت",
                                     error_messages={'required':'این فیلد الزامی است'}
                                   )
   wears = forms.ModelChoiceField(queryset=CategoryWear.objects.all(),
                                    label="نوع پوشیدنی",
                                    error_messages={'required':'این فیلد الزامی است'}
                                )
   types = forms.ModelChoiceField(queryset=CategoryTypes.objects.all(),
                                    label="نام پوشیدنی",
                                    error_messages={'required':'این فیلد الزامی است'}
                                )
   size = forms.ChoiceField(choices=SIZE,
                            label='سایز', 
                            error_messages={'required':'این فیلد الزامی است'}
                            )
   numbers = forms.CharField(label="تعداد",
                             error_messages={'required':'این فیلد الزامی است'})
   nature = forms.ModelChoiceField(queryset=Nature.objects.all(),
                                   label="جنس",
                                   error_messages={'required':'این فیلد الزامی است'}
                                )
   colors = forms.ModelMultipleChoiceField(queryset=Color.objects.all(),
                                           widget=forms.CheckboxSelectMultiple,
                                           label="رنگ ها",
                                           error_messages={'required':'این فیلد الزامی است'}
                            )
   sleeve = forms.ChoiceField(choices=SLEEVE,
                              label='نوع آستین',
                              error_messages={'required':'این فیلد الزامی است'})
   close_way = forms.ChoiceField(choices=CLOSE_WAY,
                                label='نحوه بسته شدن',
                                 error_messages={'required':'این فیلد الزامی است'})
   colors_num = forms.ChoiceField(choices=COLORS_NUM,
                                  label='تعداد رنگبندی',
                                  error_messages={'required':'این فیلد الزامی است'})
   crotch = forms.ChoiceField(choices=CROTCH,
                              label='نوع فاق',
                              error_messages={'required':'این فیلد الزامی است'})
   sale_way = forms.ChoiceField(choices=SALE_WAY,
                                label='نحوه فروش',
                                error_messages={'required':'این فیلد الزامی است'})
   warranty = forms.ChoiceField(choices=WARRANTY,
                                label='گارانتی',
                                error_messages={'required':'این فیلد الزامی است'})
   pocket = forms.ChoiceField(choices=POCKET,
                              label='جیب',
                              error_messages={'required':'این فیلد الزامی است'})
   hat = forms.ChoiceField(choices=HAT,
                           label='کلاه',
                           error_messages={'required':'این فیلد الزامی است'})
#    Belt = forms.ChoiceField(choices=[CHOICES],
#                             label='کمربند',
#                             error_messages={'required':'این فیلد الزامی است'})
   washing_point = forms.ChoiceField(choices=WASHING_POINT,
                                     label='نکات شستشو',
                                     error_messages={'required':'این فیلد الزامی است'})
   style = forms.ChoiceField(choices=STYLE,
                             label='استایل',
                             error_messages={'required':'این فیلد الزامی است'})
   design = forms.ChoiceField(choices=DESIGN,
                              label='طرح',
                              error_messages={'required':'این فیلد الزامی است'})
   spatial_feature = forms.ChoiceField(choices=SPATIAL_FEATURE,
                                       label='ویژگی های تخصصی',
                                       required=False)
   collar = forms.ChoiceField(choices=COLLAR,
                              label='یقه',
                              error_messages={'required':'این فیلد الزامی است'})
   
#------------------------------------------------------------AddEquipmentForm--------------------------------------------------------

class AddEquipmentForm(forms.Form):
    
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
    
    name = forms.CharField(label="نام کالا",
                                   error_messages={'required':'این فیلد الزامی است'}
                                   )
    first_category = forms.ChoiceField(label="دسته بندی محصول",
                                       choices=CATE,
                                       error_messages={'required':'این فیلد الزامی است'}
                                    )
    price = forms.CharField(label="قیمت",
                            error_messages={'required':'این فیلد الزامی است'}
                                    )
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),
                                           widget=forms.CheckboxSelectMultiple,
                                           label="تگ ها",
                                           error_messages={'required':'این فیلد الزامی است'}
                                    )
    description = forms.CharField(label="توضیحات",
                                  widget=forms.Textarea,
                                  required = False
                                    )
    image = forms.ImageField(label="آپلود تصویر  کالا",
                             required = False
                                    )
    videofile = forms.FileField(label="آپلود ویدئوی کالا",
                                required = False
                                    )
    
    nature = forms.ModelChoiceField(queryset=Nature.objects.all(),
                                    label="جنس",
                                    error_messages={'required':'این فیلد الزامی است'}
                                   )
    colors = forms.ModelMultipleChoiceField(queryset=Color.objects.all(),
                                           widget=forms.CheckboxSelectMultiple,
                                           label="رنگ ها",
                                           error_messages={'required':'این فیلد الزامی است'}
    )
    weidth = forms.ChoiceField(choices=WEIDTH,
                               label='عرض طاقه پارچه',
                               error_messages={'required':'این فیلد الزامی است'}
                                   )
    height = forms.ChoiceField(choices=HEIGHT,
                               label='طول طاقه پارچه',
                               error_messages={'required':'این فیلد الزامی است'}
                                   )
    weight = forms.ChoiceField(choices=WEIGHT,
                               label='وزن پارچه',
                               required=False
                                   )
    tissue_density = forms.ChoiceField(choices=TISSUE_DENSITY,
                                       label='تراکم بافت',
                                       error_messages={'required':'این فیلد الزامی است'}
                                   )
    design = forms.ChoiceField(choices=DESIGN,
                               label='طرح',
                               error_messages={'required':'این فیلد الزامی است'}
                                   )
    using = forms.ChoiceField(choices=USING,
                              label='کاربرد پارچه',
                              error_messages={'required':'این فیلد الزامی است'}
                                   )
    colors_num = forms.ChoiceField(choices=COLORS_NUM,
                                   label='تعداد رنگبندی',
                                   error_messages={'required':'این فیلد الزامی است'}
                                   )
    sale_way = forms.ChoiceField(choices=SALE_WAY,
                                 label='نحوه فروش',
                                 error_messages={'required':'این فیلد الزامی است'}
                                   )
    warranty = forms.ChoiceField(choices=WARRANTY,
                                 label='گارانتی',
                                 error_messages={'required':'این فیلد الزامی است'}
                                   )
    washing_point = forms.ChoiceField(choices=WASHING_POINT,
                                      label='نکات شستشو',
                                      error_messages={'required':'این فیلد الزامی است'}
                                   )  
    
#-------------------------------------------------------------AddMachinForm---------------------------------------------------------

class AddMachinForm(forms.Form):
    
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
    
    name = forms.CharField(label="نام کالا",
                                   error_messages={'required':'این فیلد الزامی است'}
                                   )
    first_category = forms.ChoiceField(label="دسته بندی محصول",
                                       choices=CATE,
                                       error_messages={'required':'این فیلد الزامی است'}
                                    )
    price = forms.CharField(label="قیمت",
                            error_messages={'required':'این فیلد الزامی است'}
                                    )
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),
                                           widget=forms.CheckboxSelectMultiple,
                                           label="تگ ها",
                                           error_messages={'required':'این فیلد الزامی است'}
                                    )
    description = forms.CharField(label="توضیحات",
                                  widget=forms.Textarea,
                                  required = False
                                    )
    image = forms.ImageField(label="آپلود تصویر  کالا",
                             required = False
                                    )
    videofile = forms.FileField(label="آپلود ویدئوی کالا",
                                required = False
                                    )
    
    cylinder_bed = forms.ChoiceField(choices=CYLINDER_BED,
                                     label='صفحه کار استوانه ای',
                                     error_messages={'required':'این فیلد الزامی است'}
                                    )
    flat_bed = forms.ChoiceField(choices=FLAT_BED,
                                 label='صفحه کار تخت',
                                 error_messages={'required':'این فیلد الزامی است'}
                                    )
    ghab_mako= forms.ChoiceField(choices=GHAB_MAKO,
                                 label='سیستم قاب ماکو',
                                 error_messages={'required':'این فیلد الزامی است'}
                                    )
    ghabeliate_dokht = forms.ChoiceField(choices=GHABELIAT_DOKHT,
                                         label='قابلیت دوخت',
                                         error_messages={'required':'این فیلد الزامی است'}
                                        )
    sale_way = forms.ChoiceField(choices=SALE_WAY,
                                 label='نحوه فروش',
                                 error_messages={'required':'این فیلد الزامی است'}
                                )
    warranty = forms.ChoiceField(choices=WARRANTY,
                                 label='گارانتی',
                                 error_messages={'required':'این فیلد الزامی است'}
                                )
    mako = forms.ChoiceField(choices=MAKO,
                             label='ماکو',
                             error_messages={'required':'این فیلد الزامی است'}
                                )
    masore = forms.ChoiceField(choices=MASORE,
                               label='ماسوره',
                               error_messages={'required':'این فیلد الزامی است'}
                                )
    masore_por = forms.ChoiceField(choices=MASORE_POR,
                                   label='ماسوره پرکن',
                                   error_messages={'required':'این فیلد الزامی است'}
                                )
    nakh = forms.ChoiceField(choices=NAKH,
                             label='نخ مورد استفاده دستگاه',
                             error_messages={'required':'این فیلد الزامی است'}
                                )
    pedal = forms.ChoiceField(choices=PEDAL,
                              label='پدال',
                              error_messages={'required':'این فیلد الزامی است'}
                                )
    sozan_nakhkon = forms.ChoiceField(choices=SOZAN_NAKHKON,
                                      label='سوزن نخ کن',
                                      error_messages={'required':'این فیلد الزامی است'}
                                )
    tavan = forms.ChoiceField(choices=TAVAN,
                              label='توان ساعت و حجم کار دستگاه',
                              error_messages={'required':'این فیلد الزامی است'}
                                )
    machin_weight = forms.ChoiceField(choices=MACHIN_WEIGHT,
                                      label='وزن دستگاه',
                                      error_messages={'required':'این فیلد الزامی است'}
                                )
    type = forms.ChoiceField(choices=TYPE,
                             label='نوع چرخ خیاطی',
                             error_messages={'required':'این فیلد الزامی است'}
                                )   
   
#---------------------------------------------------------------TicketForm-----------------------------------------------------------

class OpenTicket(forms.Form):
  
  title = forms.CharField(label="موضوع تیکت",
                          max_length=50,
                          error_messages={'required': 'این فیلد الزامی است.'}
                          )
  
  description = forms.CharField(label="توضیحات",
                                widget=forms.Textarea,
                                error_messages={'required':'این فیلد الزامی است.'}
                                )
  att_file = forms.FileField(label="آپلود فایل",
                             required=False
                             )
  
#------------------------------------------------------------ReplyTicketForm------------------------------------------------------
class ReplyTicketForm(forms.Form):
    
    reply = forms.CharField(label="پاسخ تیکت",
                            widget=forms.Textarea,
                            error_messages={'required':'این فیلد الزامی است.'}
                            )
    
    att_file = forms.FileField(label="آپلود فایل",
                            required=False
                            )
    