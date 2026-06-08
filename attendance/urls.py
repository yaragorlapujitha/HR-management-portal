from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.attendance_add, name='attendance_add'),
    path('list/', views.attendance_list, name='attendance_list'),
]
