from django.urls import path
from . import views


app_name='agent'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('register/phone_register/', views.phone_register, name='phone_register'),
    path('register/phone_verify/', views.phone_verify, name='phone_verify'),
    path('register/', views.AgentRegisterView.as_view(), name='register'),
    path('train_register/', views.AgentTrainView.as_view(), name='train_register'),
    # path('register/phone_verify', views.phone_verify, name='phone_verify'),
    # path('register/personal-info', views.SellerRegisterView.as_view(), name='personal-info'),
    # path('register/commer-info', views.SellerRegisterView.as_view(), name='commer-info'),
    # path('dashboard', views.SellerDashboardView.as_view(), name='dashboard'),
    # path('logout/', views.SellerLogoutView.as_view(), name='logout'),
    path('profile/', views.AgentProfileView.as_view(), name='profile'),
    path('tprofile/', views.AgentProfileView.as_view(), name='tprofile'),
    # path("register_ecco/", views.RegisterEccoInfoUserView.as_view(), name='register_ecco'),
    # path("select_production/", views.SelectCategoryView.as_view(), name='sellect_production'),
    # path("select_cat/", views.SelectCategoryView.as_view(), name='select_cat'),
    # path("add_dress/", views.AddDressView.as_view(), name='add_dress'),
    # path("add_equ/", views.AddEquipmentView.as_view(), name='add_equ'),
    # path("add_machin/", views.AddMachinView.as_view(), name='add_machin'),
    # path("list_production/", views.ListProductionView.as_view(), name='list_production'),
    # path("detail_production/<int:id>/", views.DetailProductionView.as_view(), name='detail_production'),
    # path("create_ticket/", views.OpenTicketView.as_view(), name='create_ticket'),
    # path("show_tickets/", views.ShowTicket.as_view(), name='show_tickets'),
    # path("detail_ticket/<int:id>/", views.DetailTicket.as_view(), name='detail_ticket'),
    # path("reply_ticket/<int:id>/", views.ReplyTicketView.as_view(), name='reply_ticket'),
]
