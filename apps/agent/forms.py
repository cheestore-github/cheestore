from dataclasses import fields
from msilib.schema import CheckBox
from random import choice
import re
from django import forms
from .models import AgentUser
from apps.accounts.models import CustomUser
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.shortcuts import render, redirect, get_object_or_404

class PhoneRegisterForm(forms.Form):
    phone_number = forms.CharField(label="", help_text="مثال: 09123456789",
                                    # widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'شماره تلفن همراه خود را وارد کنید'}),
                                    # error_messages={'required':'این فیلد الزامی است'},
                                    # validators=[RegexValidator(regex='^(09)\d{9}$',message="تلفن همراه می بایست 11رقم و فقط شامل عدد باشد  ",)]
                                    )


# class UserRegisterForm(forms.ModelForm):

#     class Meta:
#         model = CustomUser
#         fields = ('name', 'family', 'phone_number', 'national_code', 'email')

# class AgentRegisterForm(forms.ModelForm):
#     cv = forms.forms.FileField(label="آپلود رزومه",
#                                   required = False,
#                                   error_messages={'required':'این فیلد الزامی است'}
#                                    )

#     class Meta:
#         model = AgentUser
#         fields = ['phone','birth_year', 'residence_city', 'agency_city', 'job_history', 'last_collab', 'schooling', 'social_media_skills', 'job_space', 'reagent', 'familiarity_with_us', 'plunge_case', 'profational_skills', 'languages', 'favorites', 'cv']

#==================================================================================================================================================

    
class UserRegisterForm(forms.ModelForm):


    phone_number = forms.CharField(label='شماره همراه',
                                   validators=[RegexValidator(regex='^(09)\d{9}$',message="تلفن همراه می بایست 11رقم و فقط شامل عدد باشد  ",)],
                                   error_messages={'required':'این فیلد الزامی است'}
                                   )
    national_code = forms.CharField(label='کد ملی',
                                    validators=[RegexValidator(message="کد ملی می بایست 10رقم و فقط شامل عدد باشد  ",)],
                                    error_messages={'required':'این فیلد الزامی است'}
                                    )
    email = forms.EmailField(label='ایمیل',
                             error_messages={'required':'این فیلد الزامی است'}
                            )
    
    class Meta:
        model = CustomUser
        fields = ['name', 'family', 'phone_number', 'national_code', 'email']

class AgentRegisterForm(forms.ModelForm):
    
    # F_W_US = [
    #     ('google','جستجو در اینترنت'),
    #     ('instagram','اینستاگرام'),
    #     ('telegram','تلگرام'),
    #     ('friends','دوستان و آشنایان'),
    #     ('others','سایر')
    # ]
        
    # phone = forms.CharField(label='تلفن ثابت',
    #                         error_messages={'required':'این فیلد الزامی است'}
    #                         )
    # birth_year = forms.CharField(label='سال تولد',
    #                              error_messages={'required':'این فیلد الزامی است'}
    #                              )
    # residence_city = forms.CharField(label='شهر محل اقامت',
    #                                  error_messages={'required':'این فیلد الزامی است'}
    #                                  )
    # agency_city = forms.CharField(label='شهر مورد تقاضا یرای نمایندگی',
    #                               error_messages={'required':'این فیلد الزامی است'}
    #                               )
    # job_history = forms.CharField(label='سوابق شغلی',
    #                               error_messages={'required':'این فیلد الزامی است'}
    #                               )
    # last_collab = forms.CharField(label='مدت همکاری در آخرین تجربه کاری',
    #                               error_messages={'required':'این فیلد الزامی است'}
    #                               )
    # schooling = forms.CharField(label='میزان تحصیلات',
    #                             error_messages={'required':'این فیلد الزامی است'}
    #                             )
    # social_media_skills = forms.CharField(label='مهارت های فضای مجازی',
    #                                       error_messages={'required':'این فیلد الزامی است'}
    #                                       )
    # job_space = forms.CharField(label='متراژ و نوع فضای کار',
    #                             error_messages={'required':'این فیلد الزامی است'}
    #                             )
    # reagent = forms.CharField(label='معرف',
    #                           error_messages={'required':'این فیلد الزامی است'}
    #                           )
    # plunge_case = forms.CharField(label='وضعیت اشتغال',
    #                               error_messages={'required':'این فیلد الزامی است'}
    #                               )
    # profational_skills = forms.CharField(label='مهارت های حرفه ای',
    #                                      error_messages={'required':'این فیلد الزامی است'}
    #                                      )
    # languages = forms.CharField(label='میزان آشنایی شما با زبان انگلیسی و یا سایر زبان ها',
    #                             error_messages={'required':'این فیلد الزامی است'}
    #                             )
    # favorites = forms.CharField(label='مزایای شغلی مورد علاقه',
    #                         error_messages={'required':'این فیلد الزامی است'}
    #                         )
    # familiarity_with_us = forms.ChoiceField(label='چگونه با ما آشنا شدید؟انخاب کنید.',
    #                                       choices = F_W_US,
    #                                       error_messages={'required':'این فیلد الزامی است'}
    #                                       )
    
    cv = forms.forms.FileField(label="آپلود رزومه",
                                  required = False
                                )
    
    class Meta:
        model = AgentUser
        fields = ['phone','birth_year','residence_city','agency_city','job_history','last_collab','schooling',
                  'social_media_skills','job_space','reagent','plunge_case','profational_skills','languages',
                  'favorites','familiarity_with_us','cv']
        
class RuleForm(forms.Form):
    rule_accept = forms.BooleanField(label='قوانین و قرارداد فوق را مطالعه کرده و میپذیرم.',
                                     required= False)
    rule_deny = forms.BooleanField(label='عدم موافقت(در اینصورت حساب کاربری شما مسدود و به منزله قطع همکاری با چی استور تلقی میگردد)',
                                    required= False)
    later_read = forms.BooleanField(label='بعداَ مطالعه میکنم',
                                required= False)