from django.db import models

# Create your models here.
class Contact(models.Model):
    id= models.IntegerField(primary_key=True, auto_created=True)
    nom = models.CharField(max_length=255, blank=True, null=False)
    prenom = models.CharField(max_length=255, blank=True, null=False)
    email = models.EmailField(max_length=255, unique=True)
    pays = models.CharField(max_length=255, blank=True, null=False)
    phone = models.CharField(max_length=255, blank=True, null=False)
    ville = models.CharField(max_length=255, blank=True, null=False)
    quartier = models.CharField(max_length=255, blank=True, null=False)
    rue = models.CharField(max_length=255, blank=True, null=False)






