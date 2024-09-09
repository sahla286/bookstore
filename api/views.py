from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from api.models import Books
from api.serializers import ProductSerializer,ProductModelSerializer,UserSerializer
from rest_framework.decorators import action
from django.contrib.auth.models import User

# Create your views here.

class ProductView(APIView):
    def get(self,request,*args,**kw):
        qs=Books.objects.all()
        serializer = ProductSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def post(self,request,*args,**kw):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            Books.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer._errors)

    
class ProductDetailsView(APIView):
    def get(self,request,*args,**kw):
        id = kw.get('id')
        qs=Books.objects.get(id=id)
        serializer = ProductSerializer(qs)
        return Response(data=serializer.data)
    
    def put(self,request,*args,**kw):
        id = kw.get('id')
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            id = kw.get('id')
            Books.objects.filter(id=id).update(**request.data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer._errors)
    
    def delete(self,request,*args,**kw):
        id = kw.get('id')
        Books.objects.filter(id=id).delete()
        return Response(data='Item deleted')

class ProductViewsetView(ModelViewSet):
    serializer_class=ProductModelSerializer
    queryset=Books.objects.all()

# custom method
    @action(methods=['GET'],detail=False)
    def categories(self,request,*args,**kw):
        qs=Books.objects.values_list('category',flat=True).distinct()
        return Response(data=qs)


class UserViewsetView(ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()