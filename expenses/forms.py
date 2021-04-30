import datetime
from django import forms
from .models import Expense, Deposit


class ExpenseForm(forms.ModelForm):
    date = forms.DateField(initial=datetime.datetime.today())

    class Meta:
        model = Expense
        fields = '__all__'


class DepositForm(forms.ModelForm):
    date = forms.DateField(initial=datetime.datetime.today())

    class Meta:
        model = Deposit
        fields = '__all__'
