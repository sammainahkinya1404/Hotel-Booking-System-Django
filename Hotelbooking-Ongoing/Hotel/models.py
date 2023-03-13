from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customers(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    FullName=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    date_joined=models.DateTimeField(auto_now_add=True, auto_now=False, null=True, blank=True)
    last_login=models.DateTimeField(auto_now_add=True, auto_now=False, null=True, blank=True)

    def __str__(self):
        return self.user.username

class Rooms(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    Room_name=models.CharField(max_length=100)
    Room_status=models.BooleanField(default=True)


