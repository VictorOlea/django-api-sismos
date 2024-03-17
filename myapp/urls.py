from django.urls import path

from . import views

urlpatterns = [
    path('', views.sismos, name='sismos'),
]
