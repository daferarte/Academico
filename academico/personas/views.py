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


class persona_APIView(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer=personasSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)