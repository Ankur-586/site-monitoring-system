from django.urls import path
from . import views

urlpatterns = [
    path('cms/', views.index, name='cms'),
]
