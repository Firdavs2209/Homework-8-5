from rest_framework import serializers
from .models import StandardModel

class StandardModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StandardModel
        fields = '__all__'
