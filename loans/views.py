from rest_framework.decorators import api_view
from rest_framework.response import Response
from loans.models import Loans
from loans.serializer import LoanSerializer
@api_view(['GET'])
def list_all_loans(request):
    loans = Loans.get_all_loans()
    serializer = LoanSerializer(instance=loans, many=True)
    return Response(serializer.data)