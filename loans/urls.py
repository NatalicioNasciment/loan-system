from django.urls import path
from loans.views import list_all_loans

urlpatterns = [
    path('api/v1/loans/', list_all_loans),
]