from django.urls import path
from . import views

app_name = 'candidato' # nome da APP 

urlpatterns = [
    path('', views.CandidatesList, name='list_candidates'), # List candidates
    path('candidates/', views.CandidateCreate, name='create_candidates'), # Create candidates
    #path('candidates/<int:pk>', views.CandidatesUpdate, name='update_candidates'), # update candidates
    #path('contacts/', ListContacts.as_view(), name='list_contacts'), # Create Contacts
    #path('contacts/<int:pk>', DetailContacts.as_view(), name='detail contacts'), # Detail Contacts
]


