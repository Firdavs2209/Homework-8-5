from rest_framework import serializers
from .models import BuildingModel


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingModel
        fields = '__all__'


