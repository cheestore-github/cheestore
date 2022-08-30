from socket import fromshare
from django import forms
from .models import Wallet, Transaction


#Bank Verification Number

class BVNForm(forms.Form):
    bvn = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'شماره تایید بانک', 'required':'required'}))


class WalletForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
       super(WalletForm, self).__init__(*args, **kwargs)
       self.fields['current_balance'].widget.attrs['readonly'] = True

    class Meta:
        model=Wallet
        exclude=['user',]
        # fields='__all__'

class TransactionForm(forms.ModelForm):
    class Meta:
        model=Transaction
        fields='__all__'