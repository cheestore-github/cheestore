from django import forms
from accounts.models import CustomUser
from .models import ProfileMrketer 
from django.core.exceptions import ValidationError


###########################################################################################################################################################################################

class ApplicationForm(forms.ModelForm):

    phone_number = forms.CharField(max_length=255, label="تلفن همراه",
                                   widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'شماره تلفن همراه خود را وارد کنید'}),
                                   error_messages={'required':'این فیلد الزامی است'}
                                   )
    name = forms.CharField(max_length=150, widget=forms.Textarea, label='نام')
    family = forms.CharField(max_length=255, widget=forms.Textarea, label='نام خانوادگی')
    national_code = forms.CharField(max_length=255, widget=forms.Textarea, label='کدملی')
    email = forms.EmailField(max_length=255, widget=forms.Textarea, label='ایمیل')
    password= forms.CharField(max_length=32,label="رمز عبور",
                                   widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'رمز عبور را وارد کنید'}),
                                   error_messages={'required':'این فیلد الزامی است'}
                                   )
    birthdate = forms.DateTimeField(label='تاریخ تولد',
                                widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'تاریخ تولد خود را وارد کنید', 'type':'date'}),
                                error_messages={'required':'این فیلد الزامی است'}
                                )
    id_number = forms.CharField(max_length=10,label='تاریخ تولد',
                                widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'شماره شناسنامه  خود را وارد کنید'}),
                                error_messages={'required':'این فیلد الزامی است'})
    Nationality = forms.CharField(max_length=64, widget=forms.Textarea, label='ملیت')
    Religion = forms.CharField(max_length=64, widget=forms.Textarea, label='مذهب')
    father_name = forms.CharField(max_length=64, widget=forms.Textarea, label='نام پدر')
    city = forms.CharField(max_length=64, widget=forms.Textarea, label='شهر')
    address = forms.CharField(max_length=512, label='تاریخ تولد',
                                widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'آدرس  خود را وارد کنید'}),
                                error_messages={'required':'این فیلد الزامی است'})
    zip_code= forms.CharField(max_length=10, widget=forms.Textarea, label='کد پستی')
    representative = forms.CharField(max_length=256, widget=forms.Textarea, label=' معرف') # 3 peaple and their phone number
    work_experience = forms.CharField(max_length=256, widget=forms.Textarea, label='تجربیات کاری')
    Familiarity_socialmedia = forms.CharField(max_length=512, widget=forms.Textarea, label='میزان آشنایی با فضای مجازی')   
    Familiarity_Language = forms.CharField(max_length=512, widget=forms.Textarea, label=' آشنایی با زبان خارجی')
    Familiarity_Marketing = forms.CharField(max_length=512, widget=forms.Textarea, label='میزان آشنایی با متد های روز بازاریابی و تبلیغات')
    Familiarity_IT = forms.CharField(max_length=256, widget=forms.Textarea, label='آشنایی با کامپیوتر')


    
    class Meta:
            model = ProfileMrketer
            fields = ['personal_image','gender','cv']




###########################################################################################################################################################################################

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

###########################################################################################################################################################################################

class MarketerLoginForm(forms.ModelForm):
    national_code = forms.CharField(label="کدملی",
                                   widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'شماره کدملی خود را وارد کنید'}),
                                   error_messages={'required':'این فیلد الزامی است'}
                                   )
    password = forms.CharField(label="رمز عبور",
                                   widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'رمز عبور را وارد کنید'}),
                                   error_messages={'required':'این فیلد الزامی است'}
                                   )

###########################################################################################################################################################################################

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('name', 'family', 'phone_number', 'national_code', 'email')
