from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from api.models import Books
from api.serializers import ProductModelSerializer,UserSerializer
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ProductViewsetView(ModelViewSet):
    serializer_class=ProductModelSerializer
    queryset=Books.objects.all()
    authentication_classes =[BasicAuthentication]
    permission_classes =[IsAuthenticated]
    
    @action(methods=['GET'],detail=False)
    def categories(self,request,*args,**kw):
        qs=Books.objects.values_list('category',flat=True).distinct()
        return Response(data=qs)
    
    @action(methods=['POST'],detail=True)
    def add_cart(self,request,*args,**kw):
        id = kw.get('pk')
        user=request.user
        item=Books.objects.get(id=id)
        user.carts_set.create(product=item)
        return Response(data='Item successfully added to cart')


class UserViewsetView(ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()