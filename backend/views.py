# views.py
from rest_framework import viewsets

from .serializers import ClientSerializer, PartSerializer, NomSerializer
from .models import Client, Part, Nom


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all().order_by('name')
    serializer_class = ClientSerializer

class PartViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all().order_by('number')
    serializer_class = PartSerializer

class NomViewSet(viewsets.ModelViewSet):
    queryset = Nom.objects.all().order_by('id')
    serializer_class = NomSerializer