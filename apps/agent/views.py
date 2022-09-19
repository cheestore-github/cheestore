from django.http import HttpResponse
from unicodedata import category
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.cache import cache
from django.urls import reverse

from apps.accounts.models import CustomUser

from .forms import (AgentRegisterForm, UserRegisterForm, RuleForm, PhoneRegisterForm)
from .models import AgentUser, Rule
from .utils import Send_sms
from django.contrib.auth import authenticate, login, logout
from django.views import View
import random
import logging
from azbankintro import iban_validate, IBANValidationException

class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'agent/enter.html')
    
#=========================================AboutUs===========================================================
class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'about.html')
    
#=========================================CommonQuestions===========================================================
class CommonQuestions(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'common_q.html')
    
#=======================================PhoneRegister========================================================
# def codeGenerate():
#     return random.randint(1000,9999)
from django_otp.oath import totp

secret_key = b'12345678901234567890'
code = totp(key=secret_key, step=30, digits=4)

def phone_register(request):
    form = PhoneRegisterForm()
    if request.method == 'POST':
        form = PhoneRegisterForm(request.POST)
        if form.is_valid():
            opt = "reg"
            register_phone = form.cleaned_data['phone_number']
            Send_sms(register_phone,opt,code)
            #cache.set(register_phone,code,180)
            
        print(register_phone, ": " ,code)
        return redirect('agent:phone_verify')
        
    return render(request, 'agent/phone_register.html', {'form':form})

#============================PhoneVerify========================================================

def phone_verify(request):
    print("code", code)
    # register_phone = request.kwargs['register_phone'].value
    # print('register_phone',register_phone)
    # c_phone=cache.get(register_phone)
    # if request.method =='POST':
    verify_code = request.GET.get('phone_verify')
    if verify_code == str(code):
        print(verify_code, "You send to the next page")
        return redirect('agent:register')
    return render(request, 'agent/phone_verify.html',{'code':code})


#===================================================================================

class AgentRegisterView(View):
        
    def get(self,request, *args, **kwargs):
        user_form = UserRegisterForm()
        agent_form = AgentRegisterForm()
        return render(request, 'agent/register.html', {'user_form': user_form, 'agent_form':agent_form})

    def post(self,request,*args, **kwargs):
        user_form = UserRegisterForm()
        agent_form = AgentRegisterForm()
        if request.method == "POST":
            user_form = UserRegisterForm(request.POST)
            agent_form = AgentRegisterForm(request.POST, request.FILES or None)
            if user_form.is_valid() and agent_form.is_valid():
                custom_user = user_form.save()
                agent = agent_form.save(commit=False)
                agent.user = custom_user
                agent.save()
                messages.success(request,'ثبت اطلاعات با موفقیت انجام شد')
                return redirect('agent:profile')
            else:
                messages.error(request, 'اطلاعات وارد شده معتبر نمی باشد')
                return render(request, 'agent/register.html', {'user_form': user_form, 'agent_form': agent_form})
        
class AgentTrainView(View):
    def get(self, request, *args, **kwargs):
        user_form = UserRegisterForm()
        return render(request, 'agent/rt.html', {'user_form': user_form})
    
    def post(self, request, *args, **kwargs):
        
        user_form = UserRegisterForm()
        if request.method=='POST':
            user_form = UserRegisterForm(request.POST)
            if user_form.is_valid():
                name = user_form.cleaned_data.get('name')
                family = user_form.cleaned_data.get('family')
                phone_number = user_form.cleaned_data.get('phone_number')
                national_code = user_form.cleaned_data.get('national_code')
                email = user_form.cleaned_data.get('email')
                obj = CustomUser.objects.create(
                    name = name,
                    family = family,
                    phone_number = phone_number,
                    national_code = national_code,
                    email = email
                )
                obj.save()
                messages.success(request, 'ثبت اطلاعات با موفقیت انجام شد.')
                return redirect('agent:tprofile') 
            else:
                messages.error(request, 'اطلاعات وارد شده معتبر نمی باشد')
                return render(request, 'agent/rt.html', {'user_form': user_form}) 
        else:
            return render(request, 'agent/rt.html', {'user_form': user_form})  
        
class AgentProfileView(View):
    def get(self,request,*args, **kwargs):
        rule_form = RuleForm()
        return render(request, 'agent/profile.html',{'rule_form': rule_form})
    
    def post(self, request, *args, **kwargs):
        rule_form = RuleForm()
        if request.method == 'POST':
            rule_form = RuleForm(request.POST)
            if rule_form.is_valid():
                rule_accept = rule_form.cleaned_data.get('rule_accept')
                rule_deny = rule_form.cleaned_data.get('rule_deny')
                later_read = rule_form.cleaned_data.get('later_read')
                user = CustomUser.objects.all().last()
                obj = Rule.objects.create(
                    user = user,
                    rule_accept = rule_accept,
                    rule_deny = rule_deny,
                    later_read = later_read
                )
                obj.save()
                print(request.get_full_path)
                if request.path == "/profile/":
                    print('aaaaaaaaaaaaaaaaaaaaaa',request.get_full_path)
                    return redirect('go-to-gateway') 
                else:
                    return redirect('t-go-to-gateway')
            else:
                messages.error(request, 'اطلاعات وارد شده معتبر نمی باشد')
                return render(request, 'agent/profile.html', {'rule_form': rule_form}) 
        else:
            return render(request, 'agent/profile.html', {'rule_form': rule_form}) 
                
                       

    # def post(self,request,*args, **kwargs):
    #     return redirect('agent:login')




