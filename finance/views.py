from django.shortcuts import render
from django.db.models import Sum
from .models import Transaction
from django.db.models.functions import TruncMonth, TruncYear

def home(request):
    category_labels = []
    category_data = []
    transactions = Transaction.objects.all()
    #find out total expense overall, then find out how much each category takes part for expenses
    total = Transaction.objects.all().annotate(Year=TruncYear('transaction_date')).aggregate(Sum('amount'))
    category_list = (Transaction.objects.all().values('category').distinct())
    for item in category_list:
        category_labels.append(item['category'])
        category_amount = Transaction.objects.filter(category = item['category']).annotate(Month=TruncMonth('transaction_date')).aggregate(Sum('amount'))
        category_amount = (category_amount['amount__sum'] / total['amount__sum']) * 100
        category_ratio = round(category_amount, 2)
        category_data.append(category_ratio)
    context = {
        'transactions': transactions,
        'category_labels': category_labels,
        'category_data': category_data
    }
    return render(request, 'finance/home.html', context)



