import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse



# Create your views here.


def index(request):
    return render(request, 'first_app/index.html')



def get_data(request):
    api_url = 'https://api.example.com/data'
    headers = {'Authorization': 'Bearer YOUR_TOKEN_HERE'}
    response = requests.get(api_url,headers=headers)
    data = response.json()
    return JsonResponse(data)