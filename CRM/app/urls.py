from django.urls import path
from . import views

urlpatterns = [
    path('adminDashBoard',views.adminDashboard, name='adminDashboard'),
    path('', views.loginPage, name='login'),
    path('register', views.register, name='register'),
    path('client', views.client, name='client'),
    path('quotations', views.quotation, name='quotations')
    
    
]
