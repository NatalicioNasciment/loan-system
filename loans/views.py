from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from loans.models import Loans
from loans.serializer import LoanSerializer
from rest_framework.permissions import IsAuthenticated
from authentication.permissions import IsOwner

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsOwner])
def list_all_loans(request):

    loans = Loans.get_all_loans()
    serializer = LoanSerializer(instance=loans, many=True)
    return Response(serializer.data)