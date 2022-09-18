from django.urls import path
from . import views


app_name='marketer'
urlpatterns = [
    path('marketer/', views.MarketerLoginView.as_view(), name='login'),
    path('marketer/register/', views.MarketerApplicationView.as_view(), name='register'),
    path('marketer/logout/', views.MarketerLogoutView.as_view(), name='logout'),
    path('marketer/profile/', views.MarketerProfileView.as_view(), name='profile'),
    path('marketer/update_profile/', views.MarketerUpdateProfileView.as_view(), name='update_profile'),
    path('marketer/change_password/', views.ChangePasswordView.as_view(), name='change_password'),
]
    
    
