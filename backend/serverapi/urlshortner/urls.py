from django.urls import path
from . import views

urlpatterns = [
    path('', views.health_check, name='health_check'),
    path('save', views.save_url, name='save_url'),
    path('<str:code>', views.get_url, name='get_url')
]