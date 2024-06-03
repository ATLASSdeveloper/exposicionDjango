from rest_framework import serializers
from .models import *

class BodegaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bodega
        fields = '__all__'

class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = '__all__'

class DetalleBodegaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleBodega
        fields = '__all__'