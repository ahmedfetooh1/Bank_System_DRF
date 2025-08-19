from django.shortcuts import render
from rest_framework import generics
from .serializers import BankAccountSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .services import ManageBankAccount

# Create your views here.


class BankAccountListView(generics.ListCreateAPIView):
    queryset = ManageBankAccount.get_all_bank_accounts()
    serializer_class = BankAccountSerializer


    

