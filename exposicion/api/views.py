from django.shortcuts import render
from rest_framework import viewsets
from .models import *

class BodegaViewSet(viewsets.ModelViewSet):
    queryset = Bodega.objects.all()
    serializer_class = BodegaSerializer