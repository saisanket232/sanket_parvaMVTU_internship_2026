from django.urls import path
from . import views

urlpatterns = [
    path('api/employees/', views.employees, name='employees'),
    path('api/employees/<int:pk>/', views.employee_detail, name='employee_detail'),
]