from django.shortcuts import render
from .models import Menu

# Create your views here.

def list(request):
    list = Menu.objects.all()
    return render(request, 'menu/index.html',{'list' : list})