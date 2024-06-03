from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializer import *

class BodegaViewSet(viewsets.ModelViewSet):
    queryset = Bodega.objects.all()
    serializer_class = BodegaSerializer

class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer

class DetalleBodegaViewSet(viewsets.ModelViewSet):
    queryset = DetalleBodega.objects.all()
    serializer_class = DetalleBodegaSerializer