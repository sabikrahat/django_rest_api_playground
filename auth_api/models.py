from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('The Username field must be set')
        if not email:
            raise ValueError('The Email field must be set')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False)
    name = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=15, unique=True, null=False)
    address = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password', 'phone', 'address', 'name']

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'users'

    def isEmailExists(self):
        return User.objects.filter(email=self.email).exists()

    def isUsernameExists(self):
        return User.objects.filter(username=self.username).exists()
    
    def isPhoneExists(self):
        return User.objects.filter(phone=self.phone).exists()
    
    def toJson(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
            "name": self.name,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
    
