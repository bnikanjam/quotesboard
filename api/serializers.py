from rest_framework import serializers

from app.models import Quote


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ('quote_txt', 'author', 'source', 'quote_img', 'user')
