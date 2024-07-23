from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from finance.models import Transaction


def index(request):
    return render(request, "finance/index.html")


@login_required
def transactions_list(request):
    transactions = Transaction.objects.filter(user=request.user)
    
    context = {
        "transactions":transactions
    }
    return render(request, "finance/transactions_list.html", context)