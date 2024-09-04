from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from api.models import Books
from api.serializers import ProductSerializer,ProductModelSerializer

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


class ProductViewsetView(ViewSet):
    def list(self,request,*args,**kw):
        qs=Books.objects.all()
        serializer=ProductModelSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    # post products
    def create(self,request,*args,**kw):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    # get a product
    def retrieve(self,request,*args,**kw):
        id = kw.get('pk')
        qs=Books.objects.get(id=id)
        serializer = ProductModelSerializer(qs)
        return Response(data=serializer.data)
    
    def update(self,request,*args,**kw):
        id = kw.get('pk')
        obj=Books.objects.get(id=id)
        serializer = ProductModelSerializer(data=request.data,instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def destroy(self,request,*args,**kw):
        id = kw.get('pk')
        Books.objects.filter(id=id).delete()
        return Response(data='Item deleted')



