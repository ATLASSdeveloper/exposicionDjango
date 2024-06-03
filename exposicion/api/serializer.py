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

    bodega_nombre = serializers.CharField(source='det_bod_bod.bod_nombre',read_only=True)
    articulo_nombre = serializers.CharField(source='det_bod_art.art_nombre',read_only=True)

    class Meta:
        model = DetalleBodega
        fields = ['det_bod_id','det_bod_cantidad','det_bod_bod','det_bod_art','bodega_nombre','articulo_nombre']