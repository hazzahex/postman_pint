from django.urls import path, include
from . import views as customer_views


urlpatterns = [
    path('', customer_views.home, name='customer_home'),
]
