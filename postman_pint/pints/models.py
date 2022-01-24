from django.db import models
from django.utils import timezone
from bartender.models import Institution, Bartender
from customer.models import Customer
from django.conf import settings


# Create your models here.

class Pint(models.Model):
    # date the pint was ordered
    date_tapped = models.DateTimeField(default=timezone.now)

    # customer who ordered the pint
    sender = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, null=False, related_name="+")

    # customer who received the pint. Can be un-received
    receiver = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, null=True, related_name="+")

    # various states Pint can be in. See settings
    status = models.IntegerField(default=0, null=False)

    # institution that poured the pint and is therefore in credit
    institution = models.ForeignKey(Institution, on_delete=models.DO_NOTHING, null=True)

    # which bartender pulled this pint
    bartender = models.ForeignKey(Bartender, on_delete=models.DO_NOTHING, null=True, related_name="+")

    # share url
    share_url = models.CharField(max_length=1000, default=settings.DEFAULT_SHARE_URL, null=False)

    def __str__(self):
        return f"date: {self.date_tapped}. sender: {self.sender}, receiver: {self.receiver}, institution: {self.institution}, bartender: {self.bartender} "

