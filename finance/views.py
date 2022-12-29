from django.shortcuts import render

transactions = [
    {
        'id': 1,
        'date': '28/12/2022 20:43',
        'account': 'Cash',
        'category': 'Food',
        'amount': 'Rs. 23.45',
        'desc': 'Pizza hut - dinner'
    },
    {
        'id': 2,
        'date': '28/12/2022 21:03',
        'account': 'account',
        'category': 'transport',
        'amount': 'Rs. 100.23',
        'desc': 'Fuel'
    },
    {
        'id': 3,
        'date': '28/12/2022 21:30',
        'account': 'card',
        'category': 'food',
        'amount': 'Rs. 20',
        'desc': 'Mcdonalds icecream'
    }
]

def home(request):
    context = {
        'transactions': transactions
    }
    return render(request, 'finance/home.html', context)



