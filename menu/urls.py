from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.list, name='list'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
