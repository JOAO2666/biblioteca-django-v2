# core/filters.py

from django_filters import rest_framework as filters
from .models import Livro

class LivroFilter(filters.FilterSet):
    titulo = filters.CharFilter(lookup_expr='icontains')
    autor = filters.CharFilter(field_name='autor__nome', lookup_expr='icontains')
    categoria = filters.CharFilter(field_name='categoria__nome', lookup_expr='icontains')
    categoria_nome = filters.CharFilter(field_name='categoria__nome', lookup_expr='startswith')
    titulo_nome = filters.CharFilter(field_name='titulo', lookup_expr='startswith')

    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'categoria', 'categoria_nome', 'titulo_nome']