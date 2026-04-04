from django.urls import path
from . import views

urlpatterns = [
    path('',           views.employee_list,     name='employee_list'),

    path('register/',  views.register_employee,  name='register_employee'),

    path('edit/<int:pk>/',   views.employee_edit,   name='employee_edit'),

    path('delete/<int:pk>/', views.employee_delete, name='employee_delete'),
]