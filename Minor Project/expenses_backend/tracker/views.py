from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import User, Transactions, TransactionCategory
from .serializers import ExpenseSerializer
class IsOwner(permissions.BasePermission):
   def has_object_permission(self, request, view, obj):
      return obj.user == request.user
   
class UserViewSet(viewsets.ModelViewSet):
   serializer_class = ExpenseSerializer
   permission_classes = [permissions.IsAuthenticated, IsOwner]
   def get_queryset(self):
       return User.objects.filter(user=self.request.user).order_by('-date')
   def perform_create(self, serializer):
       serializer.save(user=self.request.user)

class TransactionsViewSet(viewsets.ModelViewSet):
   serializer_class = ExpenseSerializer
   permission_classes = [permissions.IsAuthenticated, IsOwner]
   def get_queryset(self):
       return Transactions.objects.filter(user=self.request.user).order_by('-date')
   def perform_create(self, serializer):
       serializer.save(user=self.request.user)  

class TransactionCategoryViewSet(viewsets.ModelViewSet):
   serializer_class = ExpenseSerializer
   permission_classes = [permissions.IsAuthenticated, IsOwner]
   def get_queryset(self):
       return TransactionCategory.objects.filter(user=self.request.user).order_by('-date')
   def perform_create(self, serializer):
       serializer.save(user=self.request.user)
