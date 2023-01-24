from django.shortcuts import render
from django.db.models import Sum
from .models import Transaction
from django.db.models.functions import TruncMonth, TruncYear
from datetime import datetime
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    '''
        In home page, the personal tab opens up. Here, the intention is to show the categories of expenses available for the
        current year and month. In addition, the total expenses incurred for the current year for all months will be identified too.
        Apart from visuals, the user should perform CRUD operations on the personal tab as well as the group tab.
        The figures on visuals and transaction events will change when the user wishes to choose a different year and month
        for querying. The aforementioned intention and logic will be applied to the Group tab soon.
        This will be performed in a different function since the home page is all about initialization and setup.
    '''
    category_labels = []
    category_data = []
    total_monthly_expenses = []
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    current_year = datetime.now().date().year
    current_month = datetime.now().date().month
    current_year_transactions = Transaction.objects.filter(payer = request.user.id, transaction_date__year=current_year)
    transactions = current_year_transactions.filter(transaction_date__month=current_month)

    total = transactions.aggregate(Sum('amount'))
    category_list = (transactions.values('category').distinct())

    for month in months:
        monthly_expense = current_year_transactions.filter(transaction_date__month=month).aggregate(Sum('amount'))
        #need to render the visuals, None is not accepted in frontend hence converting all None values to 0
        if monthly_expense['amount__sum'] is None:
            monthly_expense['amount__sum'] = 0
        total_monthly_expenses.append(monthly_expense['amount__sum'])

    for item in category_list:
        category_labels.append(item['category'])
        category_amount = transactions.filter(category = item['category']).aggregate(Sum('amount'))
        category_amount = (category_amount['amount__sum'] / total['amount__sum']) * 100
        category_ratio = round(category_amount, 2)
        category_data.append(category_ratio)

    context = {
        'transactions': transactions,
        'category_labels': category_labels,
        'category_data': category_data,
        'total_monthly_expenses': total_monthly_expenses
    }
    return render(request, 'finance/home.html', context)



