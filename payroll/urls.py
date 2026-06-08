from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.payroll_add, name='payroll_add'),
    path('list/', views.payroll_list, name='payroll_list'),
]