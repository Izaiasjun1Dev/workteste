from django.urls import path
from . import views

app_name = 'candidato'

urlpatterns = [
    path('', views.CandidatesList, name='list_candidates'),
    path('candidates/', views.CandidateCreate, name='create_candidates'),
    #path('candidates/<int:pk>', views.CandidatesUpdate, name='update_candidates'),
    #path('contacts/', ListContacts.as_view(), name='list_contacts'),
    #path('contacts/<int:pk>', DetailContacts.as_view(), name='detail contacts'),
]


