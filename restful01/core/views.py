# core/views.py

from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend  # Importando o backend de filtros
from rest_framework.filters import OrderingFilter  # Importando o filtro de ordenação
from .models import Livro
from .serializers import LivroSerializer
from .filters import LivroFilter  # Importando o filtro personalizado

class LivroList(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    filterset_class = LivroFilter  # Usando o filtro personalizado
    filter_backends = (DjangoFilterBackend, OrderingFilter)  # Configurando os filtros
    ordering_fields = ['titulo', 'autor', 'categoria__nome', 'publicado_em']  # Permitir ordenação
    ordering = ['titulo']  # Ordenação padrão