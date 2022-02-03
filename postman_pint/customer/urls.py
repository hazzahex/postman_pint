from django.urls import path, include
from . import views as customer_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', customer_views.home, name='home'),
    path('credit_balance', customer_views.credit_balance, name='credit-balance'),
    path('purchase_credit', customer_views.purchase_credit, name='purchase-credit'),
    path('purchase_pint', customer_views.purchase_pint, name='purchase-pint'),
    path('customer_pints', customer_views.customer_pints, name='customer-pints'),
    path('received_pints', customer_views.received_pints, name='received-pints'),
    path('claim_pint/<int:pk>', customer_views.claim_pint, name='claim-pint'),

    path('register/', customer_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='customer/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='customer/logout.html'), name='logout'),
]
