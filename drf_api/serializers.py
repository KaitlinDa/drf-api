from rest_framework import serializers
from .models import Drf_api

class Drf_api_Serializer(serializers.ModelSerializer):
  class Meta:
    fields = ("id","owner","name","description","created_at")
    model = Drf_api



