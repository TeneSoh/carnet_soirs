from .views import formulaire_contact, infos_contact
from django.urls import path

urlpatterns = [
    path('', formulaire_contact, name='formulaire_contact'),
    path('infos/', infos_contact, name='infos_contact'),
]