from rest_framework import serializers
from api.models import Books,Carts,Reviews
from django.contrib.auth.models import User

class ProductModelSerializer(serializers.ModelSerializer):
    avg_rating=serializers.CharField(read_only=True)
    review_count=serializers.CharField(read_only=True)
    class Meta:
        model=Books
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password']

    def create(self, validated_data):
        return User.objects.create_user(**self.validated_data)
    
class CartSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    user=serializers.CharField(read_only=True) 
    product=serializers.CharField(read_only=True) 
    date=serializers.CharField(read_only=True)

    class Meta:
        model=Carts
        fields='__all__'

class ReviewSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True) 
    product=serializers.CharField(read_only=True) 
    date=serializers.CharField(read_only=True)

    class Meta:
        model=Reviews
        fields='__all__'