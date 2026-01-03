from rest_framework import serializers
from nodes.models import Nodes,Links,Family

class NodesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Nodes
        fields='__all__'

class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model=Links
        fields='__all__'

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model=Family
        fields='__all__'