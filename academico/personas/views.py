from urllib import request
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import personasSerializers,tipoDocumentoSerializers
from .models import personas, tipoDocumento
from rest_framework import status
from django.http import Http404
from django.shortcuts import render

# Create your views here.
class tipoDocumento_APIView(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer=tipoDocumentoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


class tipoDocumento_APIView_List(APIView):

    def get(self, request, format=None, *args, **kwargs):
        tpdocumento = tipoDocumento.objects.all()
        serializer = tipoDocumentoSerializers(tpdocumento, many=True)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        tipoDocumento = self.get_object(pk) #  select * from tipoDcumento where id=pk
        serializer = tipoDocumentoSerializers(tipoDocumento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        tipoDocumento = self.get_object(pk)
        tipoDocumento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class persona_APIView(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer=personasSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)