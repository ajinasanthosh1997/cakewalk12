from django.shortcuts import render, redirect
from .forms import *  # Import the form you created
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages  
from django.urls import reverse
# Import your User model

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        print('thissisis sis s s sisre equest post data',request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            print(user)
            
            messages.success(request,'you have signed up successfully!')
            return redirect('cake:log_in')
        else:
            return render(request,'cake/signup.html', {'form':form})
    form = UserRegistrationForm()

    return render(request,'cake/signup.html',{'form':form})
# Create your views here.
def index(request):
    return render(request, 'cake/index.html')

def log_in(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                
                return redirect('cake:index')  # Redirect to the 'index' page on successful login
            else:
                # Authentication failed, display an error message to the user
                return render(request, 'cake/login.html', {'login_form': login_form, 'error_message': 'Invalid credentials'})
    else:
        login_form = LoginForm()

    return render(request, 'cake/login.html', {'login_form': login_form})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Create a new ContactFormEntry instance and save it to the database
            entry = ContactFormEntry(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone_number=form.cleaned_data['phone_number'],
                how_did_you_find_us=form.cleaned_data['how_did_you_find_us']
            )
            entry.save()

            # Add a success message
            messages.success(request, 'Your message has been sent successfully.')

            # Redirect to the same page
            return redirect('cake:contact')

    else:
        form = ContactForm()

    return render(request, 'cake/contact.html', {'form': form})
    
def single(request):
    return render(request, 'cake/single-product.html') 



def product(request):
    return render(request, 'cake/product.html')  

def userprofile(request):
    user = request.user  # Assuming the user is logged in
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
    else:
        form = UserProfileForm(instance=user)
    return render(request, 'cake/user_profile.html', {'form': form})

def signout(request):
    logout(request)
    return redirect(reverse('cake:index'))     