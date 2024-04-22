from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from loans.models import Loans
from loans.serializer import LoanSerializer
from rest_framework.permissions import IsAuthenticated
from authentication.permissions import IsOwner
from rest_framework import status
from loans.permission import MyDeletePermission

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsOwner])
def list_all_loans(request):

    loans = Loans.get_all_loans()
    serializer = LoanSerializer(instance=loans, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated,IsOwner])
def create_loan(request):

    if 'owner' not in request.data:
        request.data['owner'] = request.user.id
    serializer = LoanSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def update_loan(request, loan_id):
    try:
        loan = Loans.objects.get(pk=loan_id)
    except Loans.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = LoanSerializer(loan, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated,IsOwner])
def delete_loan(request, loan_id):
    try:
        loan = Loans.objects.get(pk=loan_id)
    except Loans.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    loan.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)