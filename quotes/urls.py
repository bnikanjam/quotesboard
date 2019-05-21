from django.urls import path

from . import views

urlpatterns = [
    path('ruthere', views.index, name='index')
]