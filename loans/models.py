from django.db import models

class Loans(models.Model):
    identifier = models.AutoField(primary_key=True)
    nominal_value = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    ip_address = models.CharField(max_length=45)
    request_date = models.DateTimeField(auto_now_add=True)
    bank = models.CharField(max_length=100)
    client = models.CharField(max_length=100)

    @staticmethod
    def get_all_loans():
        return Loans.objects.all()