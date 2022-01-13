from django.db import models
from customer.models import Customer
from django.conf import settings

# Create your models here.


class Institution(models.Model):
    name = models.CharField(max_length=200, default=settings.DEFAULT_INSTITUTION_NAME, null=False)

    def __str__(self):
        return f"Institution: {self.name}"


class Bartender(models.Model):
    manager = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, null=False)
    institution = models.ForeignKey(Institution, on_delete=models.DO_NOTHING, null=False)

    def __str__(self):
        return f"Bartender: {self.institution}"

