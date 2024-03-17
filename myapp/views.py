from django.shortcuts import render
from django.http import HttpResponse
import requests

def sismos(request):
    
    respose = requests.get('https://api.gael.cloud/general/public/sismos')
    sismos = respose.json()
    #print(sismos)
    
    return render(request, "sismos.html", {'sismos':sismos})
    pass
