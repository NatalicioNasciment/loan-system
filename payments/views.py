from rest_framework.decorators import api_view
from rest_framework.response import Response
from payments.models import Payments
from payments.serializer import PaymentSerializer
@api_view(['GET'])
def list_all_payments(request):
    payments = Payments.objects.all()
    serializer = PaymentSerializer(instance=payments, many=True)
    return Response(serializer.data)