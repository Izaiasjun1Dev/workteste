from rest_framework import serializers
from .models import Candidates, Contacts


class ContactsSerilaizer(serializers.ModelSerializer):      

    class Meta:
        model = Contacts
        fields = [
            'type',
            'number'
        ]       
        
class CandidatoSerializer(serializers.ModelSerializer):
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
        fild_data = validated_data.pop('contacts')
        candidates_data = Candidates.objects.create(**validated_data)
        Contacts.objects.create(candidates=candidates_data, **fild_data)
        return candidates_data        