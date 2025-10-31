from rest_framework import serializers
from nodes.models import Nodes,Links

class NodesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Nodes
        fields='__all__'

class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model=Links
        fields='__all__'