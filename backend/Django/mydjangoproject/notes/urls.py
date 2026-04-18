from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='list'),
    path('create/', views.create_note, name='create'),
    path('delete/<int:id>/', views.delete_note, name='delete'),
]