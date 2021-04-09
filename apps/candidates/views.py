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
 
@api_view(['POST'])# Decorator api view para herança de metodos pertinentes
def CandidateCreate(request):
    """Função de listagem de todos os candidatos"""
    serializer = CandidatoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET']) # Decorator api view para herança de metodos pertinentes
def CandidatesList(request):
    """Função para criar novo candidatos no banco de dados"""
    candidates = Candidates.objects.all()
    serilizer = CandidatoSerializer(candidates, many=True)
    return Response(serilizer.data)

"""Em versoes futuras serão aprensentadadas as novas função para candidatos e contatos !!"""