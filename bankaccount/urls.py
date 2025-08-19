from django.urls import path 
from .views import BankAccountListView

app_name = 'bank_account'


urlpatterns = [
    path('bank-account/',BankAccountListView.as_view(),name='create_list_bank_account'),
]
