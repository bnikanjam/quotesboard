from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
    path('', views.show_all, name='show_all'),
    path('<int:pk>', views.show_one, name='show_one'),
    path('new', views.new, name='new'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('drop/<int:pk>', views.drop, name='drop'),
]
