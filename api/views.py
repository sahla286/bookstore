from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Books
from api.serializers import ProductSerializer

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
        return Response(data='detail of a product')
    def put(self,request,*args,**kw):
        return Response(data='Item sucessesfully updated')
    def delete(self,request,*args,**kw):
        return Response(data='Item delete')