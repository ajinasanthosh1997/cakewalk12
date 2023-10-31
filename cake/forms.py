from django import forms
from . models import *  # Import your User model (change this to match your actual model)

class UserRegistrationForm(forms.ModelForm):
    full_name=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'log-label input'}),label='Full name')
    username=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'log-label input'}),label='Email address')
    phone_number=forms.IntegerField(widget=forms.TextInput(attrs={'class': 'log-label input'}),label='Phone number')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'log-label input'}),label='*************')
    location=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'log-label input'}),label='Location (Optional)')
    
    
    class Meta:
        model = Signup  # Replace with your User model
        fields = ['full_name', 'username', 'phone_number', 'password', 'location']  # Fields to include in the form

        

    

class LoginForm(forms.Form):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'log-label input'}),label="Email address")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'log-label input'}), label="*************")  


class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'con-in'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'con-in'})
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Phone number', 'class': 'con-in'})
    )
    how_did_you_find_us = forms.ChoiceField(
        choices=[
            ('', 'How did you find us?'),
            ('searchEngine', 'Search Engine'),
            ('socialMedia', 'Social Media'),
            ('friend', 'Friend/Family Recommendation'),
            ('other', 'Other'),
        ],
        widget=forms.Select(attrs={'class': 'con-in sel'})
    )

    class Meta:
        model = ContactFormEntry
        fields = ['name', 'email', 'phone_number', 'how_did_you_find_us']
    