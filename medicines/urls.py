from django.urls import path
from .views import medicine_list, medicine_create, medicine_detail, medicine_update, medicine_delete

urlpatterns = [
    path('', medicine_list, name='index'),
    path('add/', medicine_create, name='medicine-create'),
    path('<int:pk>/', medicine_detail, name='medicine-detail'),
    path('<int:pk>/update/', medicine_update, name='medicine-update'),
    path('<int:pk>/delete/', medicine_delete, name='medicine-delete'),
]
