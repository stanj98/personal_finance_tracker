from django import forms
from .models import Transaction
import datetime

ACCOUNT = [('Cash', 'Cash'), ('Accounts','Accounts'), ('Card', 'Card')]

CATEGORIES= [
    ('Food', 'Food'),
    ('Social Life', 'Social Life'),
    ('Self-development', 'Self-development'),
    ('Transportation', 'Transportation'),
    ('Culture', 'Culture'),
    ('Household', 'Household'),
    ('Apparel', 'Apparel'),
    ('Beauty', 'Beauty'),
    ('Health', 'Health'),
    ('Education', 'Education'),
    ('Gift', 'Gift'),
    ('Other', 'Other'),
]

class TransactionCreateForm(forms.ModelForm):
    account = forms.CharField(widget=forms.Select(choices=ACCOUNT))
    category = forms.CharField(widget=forms.Select(choices=CATEGORIES))
    transaction_date = forms.DateTimeField(initial=datetime.datetime.today)
    class Meta:
        model = Transaction
        exclude = ['payer']

