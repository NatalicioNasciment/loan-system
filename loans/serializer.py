from rest_framework import serializers


class LoanSerializer(serializers.Serializer):
    identifier = serializers.IntegerField()
    nominal_value = serializers.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = serializers.DecimalField(max_digits=5, decimal_places=2)
    ip_address = serializers.CharField(max_length=45)
    request_date = serializers.DateTimeField()
    bank = serializers.CharField(max_length=100)
    client = serializers.CharField(max_length=100)