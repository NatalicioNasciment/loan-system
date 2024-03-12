from rest_framework import serializers
from loans.models import Loans

class PaymentSerializer(serializers.Serializer):
    loan = serializers.PrimaryKeyRelatedField(queryset=Loans.objects.all())
    payment_date = serializers.DateTimeField()
    payment_value = serializers.DecimalField(max_digits=10, decimal_places=2)