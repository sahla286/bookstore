from rest_framework import serializers
from api.models import Books

class ProductSerializer(serializers.Serializer):
    name=serializers.CharField()
    price=serializers.IntegerField()
    description=serializers.CharField()
    category=serializers.CharField()
    image=serializers.ImageField(required=False,default=None)

class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Books
        fields='__all__'