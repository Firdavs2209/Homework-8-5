from rest_framework import serializers
from .models import ConnectionModel


class ConnectionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectionModel
        fields = '__all__'
