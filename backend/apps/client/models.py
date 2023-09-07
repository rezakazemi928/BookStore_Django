from datetime import timedelta

from django.db import models
from django.utils import timezone
from utils.validators import mobile_validator

# * Create your models here.


class CLientModel(models.Model):
    firstname = models.CharField(max_length=100, blank=False, null=False)
    lastname = models.CharField(max_length=100, blank=False, null=False)
    username = models.CharField(max_length=100, blank=False, null=False, unique=True)
    email = models.EmailField(max_length=255, blank=True, null=True, unique=True)
    mobile = models.CharField(validators=[mobile_validator()], max_length=17, blank=True)
    registration_date = models.DateTimeField(
        blank=False, null=False, default=timezone.now
    )
    expires_at = models.DateTimeField(
        blank=False, null=False, default=timezone.now() + timedelta(days=365)
    )
