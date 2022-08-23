from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterUserForm, LoginUserForm
from .models import CustomUser
from django.views import View

class RegisterUserView(View):   
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request, *args, **kwargs):
        form = RegisterUserForm()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self,request,*args, **kwargs):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data
            CustomUser.objects.create_user(
                name = user['name'],
                family= user['family'],
                phone_number = user['phone_number'],
                national_code= user['national_code'],
                email= user['email'],
                password = user['password'],
            )
            messages.success(request,'ثبت نام با موفقیت انجام شد')
            return redirect('accounts:profile')
        else:
            messages.error(request, 'اطلاعات وارد شده معتبر نمی باشد')
            return render(request, 'accounts/register.html', {'form': form})


class LoginUserView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main:index')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request, *args, **kwargs):
        form = LoginUserForm()
        return render(request,'accounts/login.html', {'form':form})

    def post(self,request,*args, **kwargs):
        form = LoginUserForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            user=authenticate(request, username=form['phone_number'], password=form['password'])
            if user is not None:
                messages.success(request, 'ورود شما با موفقیت انجام شد')
                login(request,user)
                next_url=request.GET.get('next')
                if next_url is not None:
                    return redirect(next_url)
                else:
                    return redirect('accounts:profile')
            else:
                messages.warning(request,'کاربر با این مشخصات یافت نشد')
                return render(request, 'accounts/login.html', {'form':form})
        else:
            messages.error(request, 'اطلاعات وارد شده معتبر نمی باشد')
            return render(request, 'accounts/login.html', {'form':form})


class LogoutUserView(View):    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request, *args, **kwargs):
        logout(request)
        messages.warning(request, 'خروج شما با موفقیت انجام شد')
        return redirect('accounts:login')



class ProfileView(View):
    def get(self,request,*args, **kwargs):
        return render(request, 'accounts/profile.html',{'form':'form'})

    def post(self,request,*args, **kwargs):
        pass