from socket import fromshare
from django import forms
from .models import CustomUser
from django.core.validators import EmailValidator, RegexValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='رمز عبور', widget=forms.PasswordInput)
    password2 = forms.CharField(label='تایید رمز عبور', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('name','family','phone_number','national_code','email')

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


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ('name','family','phone_number','national_code','email', 'password', 'is_active', 'is_admin')

def email_validation_function(value):
    emailvalidator = EmailValidator(message='ایمیل وارد شده نامعتبر است')
    emailvalidator(value)
    return value

def phone_number_validator():
    return RegexValidator(r'^(09)\d{9}$','شماره تلفن همراه وارد شده معتبر نمی باشد') 


class RegisterUserForm(forms.Form):
    name = forms.CharField(label="",
                                   widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام خود را وارد کنید'}),
                                   )
    family = forms.CharField(label="",
                                   widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':' نام خانوادگی خود را وارد کنید'}),
                                   )
    phone_number = forms.CharField(label="", help_text="مثال: 09123456789",
                                   widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'شماره تلفن همراه خود را وارد کنید'}),
                                   error_messages={'required':'این فیلد الزامی است'},
                                   validators=[RegexValidator(regex='^(09)\d{9}$',message="تلفن همراه می بایست 11رقم و فقط شامل عدد باشد  ",)]
                                   )
    national_code = forms.CharField(label="",
                                   widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'کدملی خود را وارد کنید'}),
                                   error_messages={'required':'این فیلد الزامی است'}
                                    )
    email = forms.EmailField(label="",
                                   widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'آدرس ایمیل خود را وارد کنید'}),
                                   error_messages={'required':'این فیلد الزامی است','invalid':'ایمیل وارد شده معتبرنمی باشد'},
                                   validators=[RegexValidator(regex='^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.\w{2,}$',message="فرمت آدرس ایمیل صحیح نمی باشد",)]
                                   )                                   
    password = forms.CharField(label="",
                                   widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'رمز عبور را وارد کنید'}),
                                   error_messages={'required':'این فیلد الزامی است'}
                                   )
    confirm_password = forms.CharField(label="",
                                   widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'رمز عبور را تکرار کنید'}),
                                   error_messages={'required':'این فیلد الزامی است'}
                                   )


    def clean_phone_number(self):
        phone_number=self.cleaned_data['phone_number']
        if CustomUser.objects.filter(phone_number=phone_number).exists():
            raise ValidationError('تلفن همراه وارد شده قبلا در سامانه ثبت نام شده است')
        return phone_number


    def clean_national_code(self):
        national_code=self.cleaned_data['national_code']
        if CustomUser.objects.filter(national_code=national_code).exists():
            raise ValidationError('کدملی وارد شده تکراری است')
        return national_code


    def clean_email(self):
        email=self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError('ایمیل وارد شده تکراری است')
        return email


    def clean(self):
        password=self.cleaned_data['password']
        confirm_password=self.cleaned_data['confirm_password']
        if password and confirm_password and password != confirm_password:
            raise ValidationError('رمز عبور مطابقت ندارد')
        return super().clean()
    




class LoginUserForm(forms.Form):
    phone_number = forms.CharField(label="تلفن همراه",
                                   widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'شماره تلفن همراه خود را وارد کنید'}),
                                   error_messages={'required':'این فیلد الزامی است'}
                                   )
    password = forms.CharField(label="رمز عبور",
                                   widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'رمز عبور را وارد کنید'}),
                                   error_messages={'required':'این فیلد الزامی است'}
                                   )

