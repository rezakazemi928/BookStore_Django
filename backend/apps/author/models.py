from apps.book.models import BookModel
from django.db import models
from utils.validators import mobile_validator

# * Create your models here.


class AuthorModel(models.Model):
    firstname = models.CharField(max_length=100, null=False, blank=False)
    lastname = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=True)
    phone_number = models.CharField(
        max_length=20, validators=[mobile_validator()], null=False, blank=False
    )
    books = models.ManyToManyField(BookModel)
