from rest_framework import serializers
from .models import Price


class PriceSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = {'nameService','content','Price'}