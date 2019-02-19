from django.shortcuts import render
from soda import settings
from .models import Menu

# Create your views here.

def list(request):
    burger_list = Menu.objects.values().filter(category_id=1)
    chicken_list = Menu.objects.values().filter(category_id=2)
    dessert_list = Menu.objects.values().filter(category_id=3)
    drink_list = Menu.objects.values().filter(category_id=4)
    package_list = Menu.objects.values().filter(category_id=5)
    return render(request, 'menu/-index.html', {
        'burger_list' : burger_list,
        'chicken_list' : chicken_list,
        'dessert_list' : dessert_list,
        'drink_list' : drink_list,
        'package_list' : package_list,
        'MEDIA_URL' : settings.MEDIA_URL,
    })
