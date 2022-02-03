from pints.models import Pint
import random


def get_pints():
    pint_list = Pint.objects.all()
    return pint_list


def get_pint(pk):
    pint = Pint.objects.get(pk=pk)
    return pint


def get_received_pints(request):
    customer = request.user.customer
    received_pints = Pint.objects.filter(receiver=customer)
    return received_pints


def generate_share_url():
    hash = random.getrandbits(128)
    return 'https://www.postman_pint.com/pint/' + str(hash)


def purchase_pint(request):
    new_pint = Pint(
        sender=request.user.customer,
        share_url=generate_share_url()
    )
    new_pint.save()
    customer = request.user.customer
    customer.credits -= 1
    customer.save()


def get_customer_pints(request):
    customer_pints = Pint.objects.filter(sender=request.user.customer)
    print(customer_pints)
    if len(customer_pints) == 0:
        print(f'No pints assigned to user')
    return customer_pints
