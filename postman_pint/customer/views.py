from django.shortcuts import render, redirect
import customer.utils as customer_utils
from pints import utils as pints_utils
from bartender import utils as bartender_utils
from .forms import UserRegisterForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def home(request):
    context = {
        "customers": customer_utils.get_customers,
        "bartenders": bartender_utils.get_bartenders,
        "institutions": bartender_utils.get_institutions,
        "pints": pints_utils.get_pints
    }
    return render(request, 'customer/home.html', context=context)


def create_pint(request):
    context = {
        'customer': request.user.customer
    }
    return render(request, 'customer/create_pint.html', context=context)


def generate_pint(request):
    """
    param request: takes the logged in user object for reference

    checks if user has any credits
    generate pint instance in database
    takes 1 credit from customer model

    if the customer doesn't have any credits, redirect to credit purchase page

    return: render share pint page with QR code and other sharable components
    """

    if request.user.customer.credits > 0:
        customer = request.user.customer
        customer.credits -= 1
        customer.save()
        new_pint = pints_utils.create_pint

        context = {
            'new_pint': new_pint
        }
        return render(request, 'customer/share_pint.html', context=context)
    else:
        return redirect('purchase-credit')


def purchase_credit(request):
    context = {
        'customer': request.user.customer
    }
    return render(request, 'customer/purchase_credit.html')
