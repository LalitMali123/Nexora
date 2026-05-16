from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('health/', views.health_check, name='health'),
    path('setup/', views.setup_database, name='setup'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('transactions/', views.TransactionListCreateView.as_view(), name='transaction-list'),
    path('transactions/<int:pk>/', views.TransactionDetailView.as_view(), name='transaction-detail'),
    path('categories/', views.CategoryListCreateView.as_view(), name='category-list'),
    path('budgets/', views.BudgetListCreateView.as_view(), name='budget-list'),
    path('budgets/<int:pk>/', views.BudgetDetailView.as_view(), name='budget-detail'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]
