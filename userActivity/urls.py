from django.urls import path
from . import views

urlpatterns = [
    path('users/',views.get_current_users,name='users'),
    path('get_ip/',views.get_client_ip,name='get_ip')   
]
