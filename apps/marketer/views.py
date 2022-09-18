
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ProfileMrketer
from accounts.models import CustomUser
from .forms import ApplicationForm,MarketerLoginForm, UserRegisterForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
import random


#=================================MarketerLogin===================================================

class MarketerLoginView(View):

    
    def get(self,request, *args, **kwargs):
        form = MarketerLoginForm()
        return render(request,'marketer.html', {'form':form})

    def post(self,request,*args, **kwargs):
        form = MarketerLoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('national_code')
            password=form.cleaned_data.get('password')
            user = authenticate(
            username=username,
            password=password
            )
            x = ProfileMrketer.objects.get('is_active')
            if x is True and user is not None:
                messages.success(request,'خوش آمدید')
                login(request,user)
                next_url=request.GET.get('next')
                if next_url is not None:
                    return redirect(next_url)

                return redirect('marketer:profile')

            else:
                messages.warning(request,'کاربر با این مشخصات یافت نشد')
                return render(request, 'marketer.html', {'form':form})
        else:
            messages.error(request, 'اطلاعات وارد شده معتبر نمی باشد')
            return render(request, 'marketer.html', {'form':form})

#============================MarketerLogout========================================================

class MarketerLogoutView(View):    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('marketer:login')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request, *args, **kwargs):
        logout(request)
        messages.warning(request, 'خروج شما با موفقیت انجام شد')
        return redirect('marketer:login')

#=================================MarketerRegister===================================================

class MarketerApplicationView(View):
    def get(self,request, *args, **kwargs):
        user_form = UserRegisterForm()
        marketer_form = ApplicationForm()
        return render(request, 'marketer/register.html', {'user_form': user_form, 'marketer_form':marketer_form})

    def post(self,request,*args, **kwargs):
        user_form = UserRegisterForm(request.POST)
        marketer_form = ApplicationForm(request.POST, request.FILES)
        if user_form.is_valid() and marketer_form.is_valid():
            custom_user = user_form.save()
            marketer = marketer_form.save(commit=False)
            marketer.user = custom_user
            marketer.save()
            messages.success(request,'ثبت نام با موفقیت انجام شد')
            return redirect('marketer:login')
        else:
            messages.error(request, 'اطلاعات وارد شده معتبر نمی باشد')
            return render(request, 'seller/register.html', {'user_form': user_form, 'marketer_form': marketer_form})

#=============================MarketerProfile=======================================================

class MarketerProfileView(View):
    def get(self,request,*args, **kwargs):
        user=request.user
        marketer=ProfileMrketer.objects.get(user=user)
        return render(request, 'marketer/profile.html', {'user':user, 'marketer':marketer})


#=============================MarketerUpdateProfile=======================================================

class MarketerUpdateProfileView(View):
    def get(self,request,*args, **kwargs):
        user_form = ApplicationForm(instance=request.user)
        return render(request, 'marketer/update_profile.html',{'user_form':user_form})

    def post(self,request,*args, **kwargs):
        user_form = UserProfileForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'پروفایل شما با موفقیت ویرایش شد')
            return redirect('marketer:profile')
        else:
            messages.error(request, 'اطلاعات وارد شده معتبر نمی باشد')
            return render(request, 'marketer/update_profile.html', {'user_form': user_form})

#=============================ChangePassword=======================================================


from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'marketer/change_password.html'
    success_message = "رمز عبور با موفقیت تغییر کرد"
    success_url = reverse_lazy('marketer:Profilemarketer')




