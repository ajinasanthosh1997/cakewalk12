# views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings  # Import Django settings
import stripe

from .forms import PaymentForm  # Import your PaymentForm from your forms.py

def cart(request):
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            stripe.api_key = settings.STRIPE_SECRET_KEY
            amount = 1672  # Total amount in cents

            try:
                # Create a Stripe payment intent
                intent = stripe.PaymentIntent.create(
                    amount=amount,
                    currency="usd",
                    description="Cake purchase",
                )

                return JsonResponse({"clientSecret": intent.client_secret})

            except Exception as e:
                return JsonResponse({"error": str(e)})
    else:
        form = PaymentForm()

    return render(request, "cart/cart.html", {"form": form})
