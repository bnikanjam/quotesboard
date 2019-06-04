from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app.urls')),
    path(r'accounts/', include('django_registration.backends.activation.urls')),
    path(r'accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
