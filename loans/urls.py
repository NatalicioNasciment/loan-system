from django.urls import path
from loans.views import list_all_loans, create_loan, delete_loan

urlpatterns = [
    path('api/v1/loans/', list_all_loans),
    path('api/v1/loan/', create_loan),
    path('api/v1/loans/<int:loan_id>/', delete_loan),

]