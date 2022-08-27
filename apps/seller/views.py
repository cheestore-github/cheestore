from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import SellerRegisterForm, UserRegisterForm, SellerLoginForm, PhoneRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.views import View
import random


class SellerRegisterView(View):
    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         return redirect('seller:login')
    #     return super().dispatch(request, *args, **kwargs)
        
    def get(self,request, *args, **kwargs):
        user_form = UserRegisterForm()
        seller_form = SellerRegisterForm()
        return render(request, 'seller/register.html', {'user_form': user_form, 'seller_form':seller_form})

    def post(self,request,*args, **kwargs):
        user_form = UserRegisterForm(request.POST)
        seller_form = SellerRegisterForm(request.POST)
        if user_form.is_valid() and seller_form.is_valid():
            custom_user = user_form.save()
            seller = seller_form.save(commit=False)
            seller.user = custom_user
            seller.save()
            messages.success(request,'ثبت نام با موفقیت انجام شد')
            return redirect('seller:login')
        else:
            messages.error(request, 'اطلاعات وارد شده معتبر نمی باشد')
            return render(request, 'seller/register.html', {'user_form': user_form, 'seller_form': seller_form})



class SellerLoginView(View):
    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         return redirect('seller:login')
    #     return super().dispatch(request, *args, **kwargs)
    
    def get(self,request, *args, **kwargs):
        form = SellerLoginForm()
        return render(request,'seller/login.html', {'form':form})

    def post(self,request,*args, **kwargs):
        form = SellerLoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('phone_number')
            password=form.cleaned_data.get('password')
            user = authenticate(
            username=username,
            password=password
            )
            if user is not None:
                messages.success(request, 'ورود شما با موفقیت انجام شد')
                login(request,user)
                next_url=request.GET.get('next')
                if next_url is not None:
                    return redirect(next_url)
                else:
                    return redirect('seller:dashboard')
            else:
                messages.warning(request,'کاربر با این مشخصات یافت نشد')
                return render(request, 'seller/login.html', {'form':form})
        else:
            messages.error(request, 'اطلاعات وارد شده معتبر نمی باشد')
            return render(request, 'seller/login.html', {'form':form})



class SellerLogoutView(View):    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('seller:login')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request, *args, **kwargs):
        logout(request)
        messages.warning(request, 'خروج شما با موفقیت انجام شد')
        return redirect('seller:login')


class SellerProfileView(View):
    def get(self,request,*args, **kwargs):
        return render(request, 'seller/profile.html',{'form':'form'})

    def post(self,request,*args, **kwargs):
        return redirect('seller:dashboard')

class SellerDashboardView(View):
    def get(self,request,*args, **kwargs):
        return render(request, 'seller/dashboard.html',{'form':'form'})

    def post(self,request,*args, **kwargs):
        pass


#====================================================================================
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
            register_phone = form.cleaned_data['phone_number']
        print(register_phone, ": " ,code)
        return redirect('seller:phone_verify')
    return render(request, 'seller/phone_register.html', {'form':form})



def phone_verify(request):
    print("code", code)
    # if request.method =='POST':
    verify_code = request.GET.get('phone_verify')
    if verify_code == str(code):
        print(verify_code, "You send to the next page")
        return redirect('seller:register')
    return render(request, 'seller/phone_verify.html',{'code':code})


#===================================================================================
