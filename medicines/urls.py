from django.urls import path
from .views import medicine_list, medicine_create, medicine_detail, medicine_edit, medicine_delete

app_name = 'medicines'

urlpatterns = [
    path('', medicine_list, name='list'),
    path('add/', medicine_create, name='create'),
    path('<int:pk>/', medicine_detail, name='detail'),
    path('<int:pk>/edit/', medicine_edit, name='edit'),
    path('<int:pk>/delete/', medicine_delete, name='delete'),
]
