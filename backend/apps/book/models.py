from datetime import datetime

from apps.admins.models import AdminModel
from apps.client.models import CLientModel
from django.db import models
from django.utils import timezone

# * Create your models here.


class BookModel(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    released_date = models.DateField(null=False, blank=False)
    edition = models.CharField(max_length=50, null=False, blank=False)
    reserved_by = models.ForeignKey(CLientModel, on_delete=models.SET_NULL, null=True)
    reserved_date_time = models.DateTimeField(null=True, blank=True)
    inserted_by = models.ForeignKey(AdminModel, on_delete=models.SET_NULL, null=True)
    inserted_date_time = models.DateTimeField(
        null=False, blank=False, default=timezone.now
    )

    def __str__(self) -> str:
        return f"Book-{self.name}"

    class Meta:
        ordering = ["name"]
