from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Store
from .forms import StoreRegisterForm, UserRegisterForm, StoreLoginForm, UserProfileForm, PhoneRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.views import View
import random


#=================================StoreRegister===================================================

class StoreRegisterView(View):
    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         return redirect('seller:login')
    #     return super().dispatch(request, *args, **kwargs)
        
    def get(self,request, *args, **kwargs):
        user_form = UserRegisterForm()
        store_form = StoreRegisterForm()
        return render(request, 'store/register.html', {'user_form': user_form, 'store_form':store_form})

    def post(self,request,*args, **kwargs):
        user_form = UserRegisterForm(request.POST)
        store_form = StoreRegisterForm(request.POST, request.FILES)
        if user_form.is_valid() and store_form.is_valid():
            custom_user = user_form.save()
            store = store_form.save(commit=False)
            store.user = custom_user
            store.save()
            messages.success(request,'ثبت نام با موفقیت انجام شد')
            return redirect('store:login')
        else:
            messages.error(request, 'اطلاعات وارد شده معتبر نمی باشد')
            return render(request, 'store/register.html', {'user_form': user_form, 'store_form': store_form})

#=================================StoreLogin===================================================

class StoreLoginView(View):
    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         return redirect('store:login')
    #     return super().dispatch(request, *args, **kwargs)
    
    def get(self,request, *args, **kwargs):
        form = StoreLoginForm()
        return render(request,'store/login.html', {'form':form})

    def post(self,request,*args, **kwargs):
        form = StoreLoginForm(request.POST)
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
                    return redirect('store:dashboard')
            else:
                messages.warning(request,'کاربر با این مشخصات یافت نشد')
                return render(request, 'store/login.html', {'form':form})
        else:
            messages.error(request, 'اطلاعات وارد شده معتبر نمی باشد')
            return render(request, 'store/login.html', {'form':form})

#============================StoreLogout========================================================

class StoreLogoutView(View):    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('store:login')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request, *args, **kwargs):
        logout(request)
        messages.warning(request, 'خروج شما با موفقیت انجام شد')
        return redirect('store:login')

#=============================StoreProfile=======================================================
from apps.accounts.models import CustomUser

class StoreProfileView(View):
    def get(self,request,*args, **kwargs):
        user=request.user
        store = Store.objects.get(user=user)
        return render(request, 'store/profile.html', {'user':user, 'store':store})


#=============================StoreUpdateProfile=======================================================

class StoreUpdateProfileView(View):
    def get(self,request,*args, **kwargs):
        user_form = UserProfileForm(instance=request.user)
        store_form = StoreRegisterForm(instance=request.user.selleruser)
        return render(request, 'store/update_profile.html',{'user_form':user_form, 'store_form':store_form})

    def post(self,request,*args, **kwargs):
        user_form = UserProfileForm(request.POST, instance=request.user)
        store_form = StoreRegisterForm(request.POST, request.FILES, instance=request.user.selleruser)
        if user_form.is_valid() and store_form.is_valid():
            user_form.save()
            store_form.save()
            messages.success(request, 'پروفایل شما با موفقیت ویرایش شد')
            return redirect('store:dashboard')
        else:
            messages.error(request, 'اطلاعات وارد شده معتبر نمی باشد')
            return render(request, 'store/update_profile.html', {'user_form': user_form, 'store_form': store_form})

#=============================ChangePassword=======================================================


from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'store/change_password.html'
    success_message = "رمز عبور با موفقیت تغییر کرد"
    success_url = reverse_lazy('seller:dashboard')

#=============================SellerDashboard=======================================================

class StoreDashboardView(View):
    def get(self,request,*args, **kwargs):
        return render(request, 'store/dashboard.html',{'form':'form'})

    def post(self,request,*args, **kwargs):
        pass


#============================PhoneRegister========================================================
# def codeGenerate():
#     return random.randint(1000,9999)
from django_otp import totp

secret_key = b'12345678901234567890'
code = totp(key=secret_key, step=30, digits=4)

def phone_register(request):
    form = PhoneRegisterForm()
    if request.method == 'POST':
        form = PhoneRegisterForm(request.POST)
        if form.is_valid():
            register_phone = form.cleaned_data['phone_number']
        print(register_phone, ": " ,code)
        return redirect('store:phone_verify')
    return render(request, 'store/phone_register.html', {'form':form})

#============================PhoneVerify========================================================

def phone_verify(request):
    print("code", code)
    # if request.method =='POST':
    verify_code = request.GET.get('phone_verify')
    if verify_code == str(code):
        print(verify_code, "You send to the next page")
        return redirect('store:register')
    return render(request, 'store/phone_verify.html',{'code':code})


#===================================================================================
