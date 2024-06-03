from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework import status


class BodegaViewSet(viewsets.ModelViewSet):
    queryset = Bodega.objects.all()
    serializer_class = BodegaSerializer

    # sobreescritura get
    def get_queryset(self):
        return Bodega.objects.filter(bod_eliminado="no")

    # sobreescritura delete
    def destroy(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        try:
            bodega = Bodega.objects.get(bod_id=id)
            bodega.bod_eliminado = "si"
            bodega.save()

            detalleBodega = DetalleBodega.objects.filter(det_bod_bod_id=id)
            detalleBodega.update(det_bod_eliminado = "si")
            
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Bodega.DoesNotExist:
            return Response({'error': 'Bodega no encontrada'}, status=status.HTTP_404_NOT_FOUND)
    
    #retrive(self, request, *args, **kwargs)
    #perform_create(self, serializer)
    #update(self, request, *args, **kwargs):
    #


class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer

class DetalleBodegaViewSet(viewsets.ModelViewSet):
    queryset = DetalleBodega.objects.all()
    serializer_class = DetalleBodegaSerializer

    # sobreescritura get
    def get_queryset(self):
        return DetalleBodega.objects.filter(det_bod_eliminado="no")

    