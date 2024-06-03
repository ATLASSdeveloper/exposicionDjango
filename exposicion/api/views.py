from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action


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

    @action(detail=False, methods=['get'])
    def obtener_filtro_articulos(self, request):
        articulo = request.query_params.get('articulo', None)

        if articulo is not None and articulo is not 'null':
            inmuebles = Articulo.objects.filter(art_nombre__icontains=articulo) #__iexact
            serializer = self.get_serializer(inmuebles, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'NO SE PROPORCIONO EL CAMPO'}, status=status.HTTP_400_BAD_REQUEST)

class DetalleBodegaViewSet(viewsets.ModelViewSet):
    queryset = DetalleBodega.objects.all()
    serializer_class = DetalleBodegaSerializer

    # sobreescritura get
    def get_queryset(self):
        return DetalleBodega.objects.filter(det_bod_eliminado="no")
    

    