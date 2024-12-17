from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #data="get all data from database"
    return render(request,'index.html')
