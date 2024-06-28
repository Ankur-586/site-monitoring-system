from django.urls import path
from . import views

urlpatterns = [
    path('cms/', views.cust_cms, name='cms'),
]
