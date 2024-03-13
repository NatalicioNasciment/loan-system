from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from payments.models import Payments
from payments.serializer import PaymentSerializer
from rest_framework.permissions import IsAuthenticated
from authentication.permissions import IsOwner

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsOwner])
def list_all_payments(request):
    payments = Payments.objects.all()
    serializer = PaymentSerializer(instance=payments, many=True)
    return Response(serializer.data)