from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
from django.dispatch import receiver


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credits = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}"


# ensures that when a user is created, they are assigned a new Customer object
@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)


# ensures whenever the User updates their info, the Customer instance is also saved.
@receiver(post_save, sender=User)
def save_user_customer(sender, instance, **kwargs):
    instance.customer.save()