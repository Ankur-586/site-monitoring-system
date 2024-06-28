from django.shortcuts import render

def cust_cms(request):
    return render(request, 'table.html')
