from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.db.models import Sum, Q
from django.utils import timezone
from .models import Transaction, Category, Budget, UserProfile
from .serializers import (
    RegisterSerializer, TransactionSerializer,
    CategorySerializer, BudgetSerializer
)

# Health check view
@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request):
    return Response({'status': 'ok', 'message': 'Server is running!'})

class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

class TransactionListCreateView(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

class CategoryListCreateView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        return Category.objects.all()
    
    def perform_create(self, serializer):
        serializer.save()

class BudgetListCreateView(generics.ListCreateAPIView):
    serializer_class = BudgetSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BudgetDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BudgetSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_view(request):
    # Get all transactions for the user (no date filter)
    all_transactions = Transaction.objects.filter(user=request.user)
    
    # Calculate totals
    total_income = all_transactions.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expenses = all_transactions.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0
    balance = total_income - total_expenses
    
    # Get recent transactions (last 10)
    recent_transactions = all_transactions.order_by('-date')[:10]
    
    return Response({
        'total_income': float(total_income),
        'total_expenses': float(total_expenses),
        'balance': float(balance),
        'recent_transactions': TransactionSerializer(recent_transactions, many=True).data
    })