from django.urls import path
from loans.views import list_all_loans, create_loan, delete_loan

app_name = 'loan'

urlpatterns = [
    path('api/v1/loans/', list_all_loans, name='all'),
    path('api/v1/loan/', create_loan, name='create'),
    path('api/v1/loans/<int:loan_id>/', delete_loan, name='delete'),

]