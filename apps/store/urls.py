from django.urls import path
from . import views


app_name='store'
urlpatterns = [
    path('', views.StoreLoginView.as_view(), name='login'),
    path('register/', views.StoreRegisterView.as_view(), name='register'),
    path('register/phone_register/', views.phone_register, name='phone_register'),
    path('register/phone_verify/', views.phone_verify, name='phone_verify'),
    path('register/personal-info/', views.StoreRegisterView.as_view(), name='personal-info'),
    path('register/commer-info/', views.StoreRegisterView.as_view(), name='commer-info'),
    path('dashboard/', views.StoreDashboardView.as_view(), name='dashboard'),
    path('logout/', views.StoreLogoutView.as_view(), name='logout'),
    path('profile/', views.StoreProfileView.as_view(), name='profile'),
    path('update_profile/', views.StoreUpdateProfileView.as_view(), name='update_profile'),
    path('change_password/', views.ChangePasswordView.as_view(), name='change_password'),
]