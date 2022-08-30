from django.urls import path
from . import views

app_name="wallet"
urlpatterns = [    
    path("webhooks/wallets_africa/aDshFhJjmIalgxCmXSj/", views.webhook, name = "webhook"),
    path("create/", views.create_wallet, name="create_wallet")
    ]