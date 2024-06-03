from django.urls import path, include
from rest_framework import routers
from api import views
from .views import *

router = routers.DefaultRouter()
router.register(r'bodega',views.BodegaViewSet)
router.register(r'articulo',views.ArticuloViewSet)
router.register(r'detalle_bodega',views.DetalleBodegaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]