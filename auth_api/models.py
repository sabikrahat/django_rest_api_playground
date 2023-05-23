from django.db import models


# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=50, unique=True, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False)
    password = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=15, unique=True, null=False)
    address = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=255, null=False)

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
            "password": self.password,
            "phone": self.phone,
            "address": self.address,
            "name": self.name,
            "created_at": self.created_at
        }