from customer.models import Customer


def get_customers():
    customers = Customer.objects.all()
    return customers


def add_credit(request):
    user = request.user
    user.customer.credits += 1
    user.save()