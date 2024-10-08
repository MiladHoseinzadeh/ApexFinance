from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from finance.filters import TransactionFilter
from finance.models import Transaction


def index(request):
    return render(request, "finance/index.html")


@login_required
def transactions_list(request):
    transaction_filter = TransactionFilter(
        request.GET,
        queryset=Transaction.objects.filter(user=request.user).select_related("category")
    )
    
    context = {
        "transaction_filter":transaction_filter
    }

    if request.htmx:
        return render(request, "finance/partials/transactions_container.html", context)

    return render(request, "finance/transactions_list.html", context)