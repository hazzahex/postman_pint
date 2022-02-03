from django.contrib.auth.decorators import login_required
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
    return render(request, 'customer/register.html', {'form': form})


@login_required
def home(request):
    context = {
        "customers": customer_utils.get_customers,
        "bartenders": bartender_utils.get_bartenders,
        "institutions": bartender_utils.get_institutions,
        "pints": pints_utils.get_pints
    }
    return render(request, 'customer/home.html', context=context)


@login_required
def credit_balance(request):
    context = {

    }
    return render(request, 'customer/credit_balance.html', context=context)


@login_required
def purchase_credit(request):
    customer_utils.add_credit(request)
    return redirect('credit-balance')


@login_required
def purchase_pint(request):
    if request.user.customer.credits > 0:
        pints_utils.purchase_pint(request)
        return redirect('customer-pints')
    else:
        return redirect('purchase-credit')


@login_required
def customer_pints(request):
    pints = pints_utils.get_customer_pints(request)
    print(f'Customer pints: {pints}')
    context = {
        'customer_pints': pints
    }
    return render(request, 'customer/customer_pints.html', context=context)


@login_required
def received_pints(request):
    context = {
        'received_pints': pints_utils.get_received_pints(request)
    }
    return render(request, 'customer/received_pints.html', context=context)


@login_required
def claim_pint(request, pk):
    pint = pints_utils.get_pint(pk)
    pint.receiver = request.user.customer
    pint.save()
    context = {
        'pint': pint
    }
    return render(request, 'pints/claim_pint.html', context=context)
