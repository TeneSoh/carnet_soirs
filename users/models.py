from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

# from users.manage import UserManager  

class UserManager(BaseUserManager) : 
    use_in_migrations = True
    def create_user(self , email , password=None , **extra_fiels) : 
        if not email : 
            raise ValueError("The email field is required")

        email = self.normalize_email(email=email)
        user = self.model(email=email , **extra_fiels)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self , email , password=None , **extra_fiels) : 
        extra_fiels.setdefault('is_staff' , True)
        extra_fiels.setdefault('is_superuser' , True)
        extra_fiels.setdefault('is_active' , True)
        extra_fiels.setdefault('is_admin' , True)

        return self.create_user(email,password,**extra_fiels)
    



class User(AbstractUser) : 
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30 , blank=True , null=True)
    bio = models.TextField(blank=True , null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager() 
    
    def __str__(self) -> str:
        return self.email