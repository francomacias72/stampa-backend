# serializers.py
from rest_framework import serializers

from .models import Client, Part, Nom

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name', 'dir1', 'dir2', 'dir3', 'rfc', 'active')

class PartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Part
        fields = ('id', 'number', 'description', 'nom_id', 'country', 'client_id' )

class NomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Nom
        fields = ('id', 'name')