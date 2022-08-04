from django.contrib import admin
from django.urls import path, include 
from ecommerce.cliente.views import ClienteViewSet
from ecommerce.produto.views import ProdutoViewSet
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register('clientes', ClienteViewSet)
router.register('produtos', ProdutoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
