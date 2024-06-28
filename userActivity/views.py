from django.shortcuts import render
from django.contrib.sessions.models import Session
from django.utils import timezone
from authenticate.models import CustomUser
from django.http import HttpResponse

def get_current_users(request):
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    user_id_list = []
    for session in active_sessions:
        data = session.get_decoded()
        user_id_list.append(data.get('_auth_user_id', None))
    # Query all logged in users based on id list
    users = CustomUser.objects.filter(id__in=user_id_list)
    all_users = ' | '.join([user.full_name for user in users])
    return HttpResponse(all_users)

def get_client_ip(request):
    # Get IP address of the client
    client_ip = request.META.get('SERVER_NAME')
    
    # Use the IP address as needed
    return HttpResponse(f"Client IP Address: {client_ip}") 

# https://docs.djangoproject.com/en/4.0/ref/request-response/#django.http.HttpRequest.META