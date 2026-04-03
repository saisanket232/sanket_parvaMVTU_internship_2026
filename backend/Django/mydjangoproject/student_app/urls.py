from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('form/', views.student_form, name='student_form'),
    path('<int:pk>/info/', views.student_info, name='student_details'),
    path('<int:pk>/edit/', views.student_edit, name='student_edit'),
    path('<int:pk>/delete/', views.student_delete, name='student_delete'),
]