from django.urls import path

from finance.views import index, transactions_list


app_name="finance"

urlpatterns = [
	path("", index, name="index"),
	path("transactions/", transactions_list, name="transactions_list"),
]
