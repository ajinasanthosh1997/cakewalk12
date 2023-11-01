
from django.urls import path
from . import views

app_name='cake'

urlpatterns = [
    
    path('',views.index,name="index"),
    path('signup/',views.signup,name="signup"),
    path('log_in/',views.log_in, name='log_in'),
    path('contact/',views.contact, name='contact'),
    path('single/<int:pk>/',views.single, name='single_product'),
    path('product/',views.products, name='products'),
    path('userprofile/',views.userprofile, name='userprofile'),
    path('signout/',views.signout, name='signout'),


]
