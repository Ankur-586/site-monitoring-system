from django.shortcuts import render
from authenticate.models import CustomUser
import requests
from django.http import JsonResponse
import time

def home(request):
    for e in CustomUser.objects.all():
        context = {
            'full_name' : e.full_name
        }
    return render(request, 'home.html',context)

def get_url_data(request):
    if request.method == 'POST':
        website_url = request.POST.get('website-url')
        # Ensure the URL starts with 'https://'
        if not website_url.startswith('https://'):
            website_url = 'https://' + website_url
        try:
            start_time = time.perf_counter()
            
            response = requests.get(website_url)

            end_time = time.perf_counter()

            # Measure response time
            response_time = response.elapsed.total_seconds()

            # Measure total load time
            load_time = end_time - start_time
            
            return JsonResponse({
                'status': response.status_code,
                'response_time': response_time,
                'load_time':load_time,
                'content': response.text 
            })
        except requests.exceptions.RequestException as e:
            return JsonResponse({
                'error': str(e)  # Convert exception to string for JSON response
            })
    return JsonResponse({
        'error': 'Invalid method'  # Example error response for other methods
    })

# ip, ssl expiry, technolgies
# PageSpeed Insights
# how do you decide the load time of a website