from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "The cart is empty")
        return redirect(reverse('vehicles'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_pk_test_51HIY8ICTFqsWfycxBmuOilOFQy8CeQQCIRnKlA3cpHahu5UEtk11mcZFuaoYm2PyurTEphZrmxbs56cwncWa8txl00OYRT99Qk',
        'client_secret': 'test_client_secret,'
    }

    return render(request, template, context)