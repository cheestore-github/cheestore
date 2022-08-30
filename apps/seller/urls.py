from django.urls import path
from . import views


app_name='seller'
urlpatterns = [
    path('', views.SellerLoginView.as_view(), name='login'),
    path('register/', views.SellerRegisterView.as_view(), name='register'),
    path('register/phone_register/', views.phone_register, name='phone_register'),
    path('register/phone_verify/', views.phone_verify, name='phone_verify'),
    path('register/personal-info/', views.SellerRegisterView.as_view(), name='personal-info'),
    path('register/commer-info/', views.SellerRegisterView.as_view(), name='commer-info'),
    path('dashboard/', views.SellerDashboardView.as_view(), name='dashboard'),
    path('logout/', views.SellerLogoutView.as_view(), name='logout'),
    path('profile/', views.SellerProfileView.as_view(), name='profile'),
    path('update_profile/', views.SellerUpdateProfileView.as_view(), name='update_profile'),
    path('change_password/', views.ChangePasswordView.as_view(), name='change_password'),
]
