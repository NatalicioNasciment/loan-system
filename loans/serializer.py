from rest_framework import serializers
from .models import Loans

class LoanSerializer(serializers.Serializer):
    identifier = serializers.IntegerField()
    nominal_value = serializers.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = serializers.DecimalField(max_digits=5, decimal_places=2)
    ip_address = serializers.CharField(max_length=45)
    request_date = serializers.DateTimeField()
    bank = serializers.CharField(max_length=100)
    client = serializers.CharField(max_length=100)

    def create(self, validated_data):
        """
        Create and return a new `Loan` instance, given the validated data.
        """
        return Loans.objects.create(**validated_data)