from enum import unique
from django.db import models


class TypeDocument(models.IntegerChoices):
    cpf = 1, 'CPF'
    cnpj = 2, 'CNPJ'


class TypeJob(models.IntegerChoices):
    pj = 1, 'PJ'
    pf = 2, 'PF'


class TypeContact(models.IntegerChoices):
    pessoal = 1, 'Pessoal'
    comercial = 2, 'Comercial'

class Contacts(models.Model):
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
    )
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
    candidato = models.ForeignKey(
        Candidates,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField('../images', blank=True)

    def __str__(self) -> str:
        return self.candidato.nome
