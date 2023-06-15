from django.shortcuts import render

# Create your views here.
from app.models import *
from app.serializers import *
from rest_framework import viewsets
from rest_framework.response import Response

class ProductData(viewsets.ViewSet):
    def list(self,request):
        PO=Product.objects.all()
        psd=ProductMS(PO,many=True)
        return Response(psd.data)

    def retrieve(self,request,pk):
        po=Product.objects.get(pk=pk)
        psd=ProductMS(po)
        return Response(psd.data)

    def create(self,request):
        psd=ProductMS(data=request.data)
        if psd.is_valid():
            psd.save()
            return Response({"The data is insertd successfully"})
        else:
            return Response({"The data is invalid"})
    def update(self,request,pk):
        PO=Product.objects.get(pk=pk)
        psd=ProductMS(po,data=request.data)
        if psd.is_valid():
            psd.save()
            return Response({"The data is updated"})
        else:
            return Response({"The data is not valid"})
    def partial_update(self,request,pk):
        PO=Product.objects.get(pk=pk)
        psd=ProductMS(po,data=request.data,partial=True)
        if psd.is_valid():
            psd.save()
            return Response({"The data is partially updated"})
        else:
            return Response({"The data is not valid"})
    def delete(self,request,pk):
        Product.objects.get(pk=pk).delete()
        return Response({"Data is deleted succssfully"})