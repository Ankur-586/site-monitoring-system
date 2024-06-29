from django.shortcuts import render
from authenticate.models import CustomUser

def home(request):
    for e in CustomUser.objects.all():
        context = {
            'full_name' : e.full_name
        }
    return render(request, 'home.html',context)