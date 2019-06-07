from rest_framework import generics
from .serializers import QuoteSerializer

from app.models import Quote


class QuoteList(generics.ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
