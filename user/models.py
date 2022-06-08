from django.db import models
from django.contrib.auth.models import User
import uuid

class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)

    # image = models.ImageField(null=True, blank=True)
    purpose = models.CharField(max_length=1000,null=True, blank=True)
    last_logged_in = models.DateTimeField(auto_now_add=True)
    email_verified = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table='profile'


class Token(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    session_token = models.CharField(max_length=300, default=uuid.uuid4, unique=True)
    logged_in = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=100, null=True, blank=True)

class ForgotDetails(models.Model):
    id =models.AutoField(primary_key=True)
    email = models.CharField(max_length=100, null=False, blank=False)
    otp = models.IntegerField(null=False, blank=False)
