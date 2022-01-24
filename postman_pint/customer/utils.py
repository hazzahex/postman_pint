from customer.models import Customer


def get_customers():
    customers = Customer.objects.all()
    return customers