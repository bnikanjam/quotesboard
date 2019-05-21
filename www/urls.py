from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('quotes.urls')),
    path('qb-backend/', admin.site.urls),
]
