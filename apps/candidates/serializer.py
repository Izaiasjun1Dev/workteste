from rest_framework import serializers
from .models import Candidates, Contacts


class ContactsSerilaizer(serializers.ModelSerializer):      
    """
    Serializador do model contacts trata os campos Type_Contacts e Number_contact
    """
    class Meta:
        model = Contacts
        fields = [
            'type',
            'number'
        ]       
        
class CandidatoSerializer(serializers.ModelSerializer):
    """
    Serializador do model Candidates trata 
    todos os campos de candidados com exceção 
    de created_at e updated_at
    """
    contacts = ContactsSerilaizer(read_only=False) 
    
    class Meta:
        model = Candidates
        fields = [
            'nome',
            'sobrenome',
            'document',
            'type_document',
            'job',
            'is_active',
            'contacts'
        ]

    def create(self, validated_data):
        """Estão função sera melhora em verçoes futuas para alem da 
        leitura aninhada do models poderá criar os 
        models de forma tambem aninhada """
        fild_data = validated_data.pop('contacts')
        candidates_data = Candidates.objects.create(**validated_data)
        Contacts.objects.create(candidates=candidates_data, **fild_data)
        return candidates_data        