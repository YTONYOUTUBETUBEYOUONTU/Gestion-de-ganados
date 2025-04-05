from django.contrib import admin
from .models import Ganaderos, Ganado, Compra, Venta, Traspaso

admin.site.register(Ganaderos)
admin.site.register(Ganado)
admin.site.register(Compra)
admin.site.register(Venta)
admin.site.register(Traspaso)