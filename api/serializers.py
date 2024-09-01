from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    name=serializers.CharField()
    price=serializers.IntegerField()
    description=serializers.CharField()
    category=serializers.CharField()
    # image=serializers.ImageField()