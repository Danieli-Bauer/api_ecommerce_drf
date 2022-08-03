from django.shortcuts import render
from .models import Produto
from .serializers import ProdutoSerializer
from rest_framework import viewsets


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer