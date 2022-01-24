from django.urls import path, include
from . import views as customer_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', customer_views.home, name='customer_home'),
    path('create_pint', customer_views.create_pint, name='create-pint'),
    path('generate_pint', customer_views.generate_pint, name='generate-pint'),
    path('purchase_credit', customer_views.purchase_credit, name='purchase-credit'),
    path('register/', customer_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='customer/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='customer/logout.html'), name='logout'),
]
