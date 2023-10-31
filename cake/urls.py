
from django.urls import path
from . import views

app_name='cake'

urlpatterns = [
    
    path('',views.index,name="index"),
    path('signup/',views.signup,name="signup"),
    path('log_in/',views.log_in, name='log_in'),
    path('contact/',views.contact, name='contact'),
    path('single/',views.single, name='single'),
    path('product/',views.product, name='product'),
    path('userprofile/',views.userprofile, name='userprofile'),
    path('signout/',views.signout, name='signout'),


]
