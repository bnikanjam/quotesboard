from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app.urls')),
    path(r'app/', include('app.urls')),
    path(r'api/', include('api.urls')),
    path(r'accounts/', include('django_registration.backends.activation.urls')),
    path(r'accounts/', include('django.contrib.auth.urls')),
    path('darposht/', admin.site.urls),
]
