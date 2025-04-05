from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GanaderosViewSet, GanadoViewSet, CompraViewSet, VentaViewSet, TraspasoViewSet

router = DefaultRouter()
router.register(r'ganaderos', GanaderosViewSet)
router.register(r'ganado', GanadoViewSet)
router.register(r'compras', CompraViewSet)
router.register(r'ventas', VentaViewSet)
router.register(r'traspasos', TraspasoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
