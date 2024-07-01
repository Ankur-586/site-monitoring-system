from django.shortcuts import render
from django.contrib.sessions.models import Session
from django.utils import timezone
from authenticate.models import CustomUser
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# @login_required
def get_current_logged_in_users(request):
    '''
    This is working fine
    '''
    # Filter active sessions
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    # Get active user IDs
    user_id_list = []
    for session in active_sessions:
        data = session.get_decoded()
        user_id = data.get('_auth_user_id')
        if user_id and user_id not in user_id_list:
            user_id_list.append(user_id)
    # Query all logged in users based on id list
    users = CustomUser.objects.filter(id__in=user_id_list)
    # Prepare response
    all_users = ' | '.join([user.full_name for user in users])
    return HttpResponse(all_users)

def get_client_ip(request):
    # Get IP address of the client
    client_ip = request.META.get('REMOTE_ADDR', '')
    # Use the IP address as needed
    return HttpResponse(f"Client IP Address: {client_ip}") 


# https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.META
# give me industry level code meaning when most senior developer write these code for login ,logout, register in django