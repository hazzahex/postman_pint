from pints.models import Pint


def get_pints():
    pint_list = Pint.objects.all()
    return pint_list


def create_pint(sender):
    new_pint = Pint(sender=sender)
    new_pint.save()
    return new_pint
