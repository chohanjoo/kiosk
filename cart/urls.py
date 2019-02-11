from django.urls import path,include
from . import views

app_name = "cart"

urlpatterns = [
    path('', views.pay, name='pay'),
]
