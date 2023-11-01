from django import forms

class PaymentForm(forms.Form):
    name_on_card = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'cart-in', 'placeholder': 'Name on card'})
    )
    card_number = forms.CharField(
        max_length=16,
        widget=forms.TextInput(attrs={'class': 'cart-in', 'placeholder': '1111 2222 3333 4444'})
    )
    expiration_date = forms.CharField(
        max_length=5,
        widget=forms.TextInput(attrs={'class': 'cart-in2', 'placeholder': 'mm/yy'})
    )
    cvv = forms.CharField(
        max_length=3,
        widget=forms.TextInput(attrs={'class': 'cart-in2', 'placeholder': '123'})
    )
