from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Wallet
from .forms import WalletForm

# Create your views here.
from cryptography.fernet import Fernet


@login_required
def create_wallet(request):
    form = WalletForm()
    user = request.user
    if request.method == 'POST':
        if form.is_valid():
            cd = form.cleaned_data
            user = request.user
            Wallet.objects.create(
                user = user,
                current_balance = cd.get('current_balance'),
                account_name = cd.get('account_name'),
                account_number = cd.get('account_number'),
                bank = cd.get('bank'),
            )
            messages.success(request, "کیف پول شما با موفقیت ایجاد شد")
            return redirect("accounts:dashboard")
        else:
            messages.error(request, "اطلاعات وارد شده صحیح نمی باشد")
           
    return render(request, "wallet/create_wallet.html", context = {"form":form, 'user':user})








from django.db import transaction
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from ipaddress import ip_address, ip_network
import json
from .models import Wallet, Transaction


@csrf_exempt
@require_POST
def webhook(request):
        whitelist_ip = "18.158.59.198"    
        forwarded_for = u'{}'.format(request.META.get('HTTP_X_FORWARDED_FOR'))    
        client_ip_address = ip_address(forwarded_for)    
        if client_ip_address != ip_network(whitelist_ip):        
            return HttpResponseForbidden('Permission denied.')
        payload = json.loads(request.body)
        if payload['EventType'] == "BankTransferFunding":
            wallet = get_object_or_404(Wallet, phone_number = payload["phoneNumber"])
            wallet.balance += payload["amount"]
            wallet.save()
            transaction =  Transaction.objects.create(            
                transaction_id = payload["transactionRef"],
                transaction_type = "funding",            
                wallet = wallet,            
                status = "success",            
                amount = payload["amount"],            
                date = payload["DateCredited"]        
                )    
        else:        
            pass    
        return HttpResponse(status=200)


