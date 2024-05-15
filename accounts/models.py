from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_valid', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(email, password, **extra_fields)
        

class CustomUser(AbstractBaseUser, PermissionsMixin):
    name=models.CharField(max_length=100)
    mobile_no=models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    password=models.CharField(unique=True)
    is_valid = models.BooleanField(default=True)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    
    def __str__(self):
        return self.email

    class Meta:
        abstract = True

