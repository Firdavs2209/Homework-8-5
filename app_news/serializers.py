from rest_framework.serializers import ModelSerializer
from .models import NewsModel,StandardsModel,UnitsModel,LeadershipModel


class NewsSerializer(ModelSerializer):
    class Meta:
        model = NewsModel
        fields = '__all__'


class StandardsSerializer(ModelSerializer):
    class Meta:
        model = StandardsModel
        fields = '__all__'


class UnitsSerializer(ModelSerializer):
    class Meta:
        model = UnitsModel
        fields = '__all__'


class LeadershipSerializer(ModelSerializer):
    class Meta:
        model = LeadershipModel
        fields = '__all__'


