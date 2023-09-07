from django.db import models

# * Create your models here.


class AdminModel(models.Model):
    firstname = models.CharField(max_length=100, blank=False, null=False)
    lastname = models.CharField(max_length=100, blank=False, null=False)
    username = models.CharField(max_length=100, blank=False, null=False, unique=True)
    email = models.EmailField(max_length=255, blank=True, null=True, unique=True)
