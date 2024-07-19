from django.urls import path

from finance.views import index


app_name="finance"

urlpatterns = [
	path("", index, name="index")
]
