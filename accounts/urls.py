from django.urls import path

from .views import register_view, login_view, logout_view, user_detail

app_name = 'accounts'

urlpatterns = [
    path('me/', user_detail, name='user-detail'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

]
