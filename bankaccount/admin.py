from django.contrib import admin
from .models import BankAccount , Transaction
# Register your models here.


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ['user','account_number','balance','is_active','created_at']
    readonly_fields = ['account_number']
    list_filter = ['is_active']



@admin.register(Transaction)
class TransactionAdimn(admin.ModelAdmin):
    list_display = ['transaction_number','transaction_type','created_at','amount','account']
    list_filter = ['transaction_type']
    readonly_fields = ['transaction_number']