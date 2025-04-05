from rest_framework import viewsets
from .models import Ganaderos, Ganado, Compra, Venta, Traspaso
from .serializers import GanaderosSerializer, GanadoSerializer, CompraSerializer, VentaSerializer, TraspasoSerializer

class GanaderosViewSet(viewsets.ModelViewSet):
    queryset = Ganaderos.objects.all()
    serializer_class = GanaderosSerializer

class GanadoViewSet(viewsets.ModelViewSet):
    queryset = Ganado.objects.all()
    serializer_class = GanadoSerializer

class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

class TraspasoViewSet(viewsets.ModelViewSet):
    queryset = Traspaso.objects.all()
    serializer_class = TraspasoSerializer
