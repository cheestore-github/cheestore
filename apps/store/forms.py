from django import forms
from .models import Store
from apps.accounts.models import CustomUser
from django.core.exceptions import ValidationError
from .validators import telephone_regex, zip_code_regex


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

class StoreRegisterForm(forms.ModelForm):
    birthdate = forms.DateField(label='تاریخ تولد', required=False,
                                widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'تاریخ تولد خود را وارد کنید', 'type':'date'}),
                                error_messages={'required':'این فیلد الزامی است'}
                                )

    class Meta:
        model = Store
        fields = ['img_profile','gender','birthdate', 'img_national_card','address']

#==================================================================================================================================================

class StoreLoginForm(forms.ModelForm):
    phone_number = forms.CharField(label="تلفن همراه",
                                   widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'شماره تلفن همراه خود را وارد کنید'}),
                                   error_messages={'required':'این فیلد الزامی است'}
                                   )
    password = forms.CharField(label="رمز عبور",
                                   widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'رمز عبور را وارد کنید'}),
                                   error_messages={'required':'این فیلد الزامی است'}
                                   )

    class Meta:
        model = Store
        fields=['phone_number', 'password']


    

#================================================================================================================================
class UserProfileForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('name', 'family', 'phone_number', 'national_code', 'email')



class StoreRegisterForm(forms.Form):
    telephone_number = forms.CharField(validators=[telephone_regex])
    zip_code = forms.CharField(validators=[zip_code_regex])
    phone_number = forms.CharField(label="", help_text="مثال: 09123456789",
                                    )


class PhoneRegisterForm(forms.Form):
    phone_number = forms.CharField(label="", help_text="مثال: 09123456789",
                                    # widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'شماره تلفن همراه خود را وارد کنید'}),
                                    # error_messages={'required':'این فیلد الزامی است'},
                                    # validators=[RegexValidator(regex='^(09)\d{9}$',message="تلفن همراه می بایست 11رقم و فقط شامل عدد باشد  ",)]
                                    )