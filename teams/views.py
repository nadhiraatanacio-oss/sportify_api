from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Equipo, Jugador
from .serializers import EquipoSerializer, JugadorSerializer


class EquipoViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['nombre', 'categoria']


class JugadorViewSet(viewsets.ModelViewSet):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'posicion']