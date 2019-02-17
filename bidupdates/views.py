from django.shortcuts import render

def home(request):
    return render(request,'bidupdates/home.html')
