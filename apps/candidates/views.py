from django.core.checks import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import (
    Candidates,
    Contacts
)
from .serializer import (
    CandidatoSerializer,
    ContactsSerilaizer
)
 
@api_view(['POST'])
def CandidateCreate(request):
    serializer = CandidatoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def CandidatesList(request):
    candidates = Candidates.objects.all()
    serilizer = CandidatoSerializer(candidates, many=True)
    return Response(serilizer.data)