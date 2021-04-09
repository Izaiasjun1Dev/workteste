from enum import unique
from django.db import models


class TypeDocument(models.IntegerChoices):
    """Choices para o tipo de documento se 1 = cpf
    se 2 = cnpj 
    """
    cpf = 1, 'CPF'
    cnpj = 2, 'CNPJ'


class TypeJob(models.IntegerChoices):
    """
    Choices para o tipo de documento se 1 = pj => pessoa juridica
    se 2 = pf => pessoa fisica 
    """
    pj = 1, 'PJ'
    pf = 2, 'PF'


class TypeContact(models.IntegerChoices):
    """
    Choices para o tipo de documento se 1 = Pessoal => Contato pessoal
    se 2 = Comercial => Contato Comercial
    """
    pessoal = 1, 'Pessoal'
    comercial = 2, 'Comercial'

class Contacts(models.Model):
    """
    Model relacional de contatos
    """
    id = models.AutoField(unique=True, auto_created=True, primary_key=True)
    type = models.IntegerField(
        default=TypeContact.pessoal,
        choices=TypeContact.choices
    )
    number = models.CharField(max_length=15, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.number

    class Meta:
        verbose_name = 'Contato'
        ordering = ('-created_at', )

class Candidates(models.Model):
    """
    Model relacional de candidatos aninhado ao modelo contato
    """
    nome = models.CharField(max_length=20, help_text='Nome')
    sobrenome = models.CharField(max_length=80, help_text='Sobrenome')
    document = models.CharField(
        max_length=20,
        unique=True,
        help_text='Somente Numeros'
    )
    type_document = models.IntegerField(
        default=TypeDocument.cpf,
        choices=TypeDocument.choices
    )
    contacts = models.ForeignKey(
        Contacts, 
        on_delete=models.CASCADE,
    ) # referencia estrnageira do model contacts
    job = models.IntegerField(
        default=TypeJob.pj, 
        choices=TypeJob.choices
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Candidato'
        ordering = ('-created_at', )

class ImageProfile(models.Model):
    """
    Model relacional de imagens, ou album de fotos para o candidato, 
    tambem aninhado ao candidato
    """
    candidato = models.ForeignKey(
        Candidates,
        on_delete=models.CASCADE,
        related_name='images'
    ) # referencia do model candidato
    image = models.ImageField('../images', blank=True)

    def __str__(self) -> str:
        return self.candidato.nome
