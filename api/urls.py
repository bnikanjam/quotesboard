from django.urls import path

from .views import QuoteList

urlpatterns = [
    path('', QuoteList.as_view()),
]
