from django.db import models
from loans.models import Loans

class Payments(models.Model):
    loan = models.ForeignKey(Loans, related_name='payments', on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_value = models.DecimalField(max_digits=10, decimal_places=2)