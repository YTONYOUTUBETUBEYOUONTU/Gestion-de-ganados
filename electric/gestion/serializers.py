from rest_framework import serializers
from .models import Ganaderos, Ganado, Compra, Venta, Traspaso

class GanaderosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ganaderos
        fields = ['id', 'nombre', 'telefono', 'direccion']

class GanadoSerializer(serializers.ModelSerializer):
    dueño = GanaderosSerializer(read_only=True)
    class Meta:
        model = Ganado
        fields = ['id', 'numero_identificacion', 'especie', 'raza', 'fecha_nacimiento', 'peso', 'dueño']

class CompraSerializer(serializers.ModelSerializer):
    ganado = GanadoSerializer(read_only=True)
    comprador = GanaderosSerializer(read_only=True)
    class Meta:
        model = Compra
        fields = ['id', 'ganado', 'comprador', 'fecha', 'precio']

class VentaSerializer(serializers.ModelSerializer):
    ganado = GanadoSerializer(read_only=True)
    vendedor = GanaderosSerializer(read_only=True)
    class Meta:
        model = Venta
        fields = ['id', 'ganado', 'vendedor', 'comprador', 'fecha', 'precio']

class TraspasoSerializer(serializers.ModelSerializer):
    ganado = GanadoSerializer(read_only=True)
    dueño_original = GanaderosSerializer(read_only=True)
    dueño_destino = GanaderosSerializer(read_only=True)
    class Meta:
        model = Traspaso
        fields = ['id', 'ganado', 'dueño_original', 'dueño_destino', 'fecha']
