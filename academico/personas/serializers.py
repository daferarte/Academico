from rest_framework import serializers
from .models import personas, tipoDocumento

class tipoDocumentoSerializers(serializers.ModelSerializer):
    class Meta:
        model = tipoDocumento
        fields = '__all__'

class personasSerializers(serializers.ModelSerializer):
    class Meta:
        model = personas
        field = '__all__'