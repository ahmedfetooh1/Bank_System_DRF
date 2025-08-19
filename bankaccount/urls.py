from django.urls import path 
from .views import BankAccountListView , transaction_view

app_name = 'bank_account'


urlpatterns = [
    path('bank-account/',BankAccountListView.as_view(),name='create_list_bank_account'),
    path('transaction/',transaction_view,name='create_list_transaction'),
]
