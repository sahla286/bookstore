from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Books,Carts,Reviews
from api.serializers import ProductModelSerializer,UserSerializer,ReviewSerializer,CartSerializer
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# Create your views here.

class UserViewsetView(ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()

class ProductViewsetView(ModelViewSet):
    authentication_classes =[BasicAuthentication]
    permission_classes =[IsAuthenticated]
    serializer_class=ProductModelSerializer
    queryset=Books.objects.all()
    
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
    
    @action(methods=['POST'],detail=True)
    def add_review(self,request,*args,**kw):
        id=kw.get('pk')
        user=request.user
        product=self.queryset.get(id=id)
        ser=ReviewSerializer(data=request.data)
        if ser.is_valid():
            ser.save(product=product,user=user)
            return Response(data=ser.data,status=status.HTTP_201_CREATED)
        return Response(data=ser.errors,status=status.HTTP_400_BAD_REQUEST)
    
class CartView(ModelViewSet):
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=Carts.objects.all()
    serializer_class=CartSerializer
    def list(self, request, *args, **kwargs):
        user=request.user
        carts=self.queryset.filter(user=user)
        ser=self.serializer_class(carts,many=True)
        return Response(data=ser.data,status=status.HTTP_200_OK)

class ReviewView(APIView):
    def delete(self, request, *args, **kw):
        id=kw.get('id')
        review=Reviews.objects.filter(id=id).first()
        if review:
            review.delete()
            return Response(data={'msg':'review deleted'},status=status.HTTP_200_OK)
        else:
            return Response(data={'msg':'review not found'},status=status.HTTP_404_NOT_FOUND)

