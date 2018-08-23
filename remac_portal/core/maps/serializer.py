from rest_framework import serializers
from remac_portal.models.maps import Map, Vertex, Edge


class SerieSerializerMap(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = ('id', 'is_active', 'numbers_floor', 'description', 'building')

"""
class SerieSerializerEdge(serializers.ModelSerializer):
    class Meta:
        model = Edge
        fields = ('id', 'name', 'numbers_floor', 'weight', 'map')

    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    numbers_floor = serializers.IntegerField()
    weight = serializers.IntegerField()
    map = serializers.F(choices=Serie.CATEGORIES_CHOICES)

    def create(self, validated_data):
        # Create and return a new `Serie` instance, given the validated data.

        return Serie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Update and return an existing `Serie` instance, given the validated data.

        instance.name = validated_data.get('name', instance.name)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance
"""

class SerieSerializerVertex(serializers.ModelSerializer):
    class Meta:
        model = Vertex
        fields = ('id', 'is_origin_point', 'nfc_code', 'name', 'has_nfc', 'edge', 'point_x', 'point_y', 'point_z')
