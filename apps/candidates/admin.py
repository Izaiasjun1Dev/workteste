from django.contrib import admin
from .models import (
    Candidates,
    Contacts,
    ImageProfile
)

class ImageInline(admin.TabularInline):
    model = ImageProfile
    extra = 2

class ContactsInline(admin.TabularInline):
    """Inlines"""
    model = Contacts

@admin.register(Candidates)
class CandidatesAdmin(admin.ModelAdmin):
    list_display = [
        'nome', 
        'job',
        'sobrenome', 
        'document', 
        'contacts',
        'is_active'
    ]
    list_filter = [
        'job',
        'is_active',
        'created_at'
    ]
    list_editable = [
        'contacts',
        'job',
        'is_active'
    ]
    inlines = [ImageInline]

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = [
        'type',
        'number'
    ]
    list_filter = [
        'type',
    ]
    list_editable = [
       'number'
    ]
 



