from django.db import models

# Create your models here.
class SignUp(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email=models.EmailField(max_length=255,unique = True)
    username = models.CharField(max_length = 255,unique = True)
    referral_code = models.CharField(max_length=16, null=True)
    score = models.IntegerField()

class SignUp2(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email=models.EmailField(max_length=255,unique = True)
    username = models.CharField(max_length = 255,unique = True)
    referral_code = models.CharField(max_length=16, null=True)
    score = models.IntegerField()
