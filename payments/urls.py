from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('', views.home, name='home'),
    path('payments/create/', views.create_payment, name='create_payment'),
    path('payments/receive/', views.receive_payment, name='receive_payment'),
    path('payments/check/', views.check_payment, name='check_payment'),

]

