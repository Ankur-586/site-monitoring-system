from django.shortcuts import render
from authenticate.models import CustomUser
import requests
from django.http import JsonResponse

def home(request):
    for e in CustomUser.objects.all():
        context = {
            'full_name' : e.full_name
        }
    return render(request, 'home.html',context)

def get_url_data(request):
    if request.method == 'POST':
        website_url = request.POST.get('website-url')
        try:
            response = requests.get(website_url)
            return JsonResponse({
                'status': response.status_code
            })
        except Exception as e:
            return JsonResponse({
                'error': str(e)  # Convert exception to string for JSON response
            })

    # Handle other HTTP methods (GET, PUT, DELETE, etc.) if needed
    return JsonResponse({
        'error': 'Invalid method'  # Example error response for other methods
    })
    