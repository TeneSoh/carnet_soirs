from django.db import models
from users.models import User
# Create your models here.

class Contact(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    nom = models.CharField(max_length=255, null=False, blank=False)
    prenom = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(null=False, unique=True)
    pays = models.CharField(max_length=255, null=False, blank=False)
    phone = models.CharField(max_length=255, null=False, blank=False)
    ville = models.CharField(max_length=255, null=False, blank=False)
    quartier = models.CharField(max_length=255, null=False, blank=False)
    rue = models.CharField(max_length=255, null=False, blank=False) 
    is_activate = models.BooleanField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')