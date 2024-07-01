from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('search_website/',views.get_url_data,name='search-website')
]
