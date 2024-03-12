from django.urls import path
from payments.views import list_all_payments

urlpatterns = [
    path('api/v1/payments/', list_all_payments),
]