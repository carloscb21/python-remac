from rest_framework import serializers
from remac_portal.models.maps import Map, Vertex, Edge


class SerieSerializerMap(serializers.ModelSerializer):
    vertexs = serializers.StringRelatedField(many=True)

    class Meta:
        model = Map
        fields = ('id', 'is_active', 'numbers_floor', 'description', 'building', 'vertexs')


class SerieSerializerVertex(serializers.ModelSerializer):

    vertex_1 = serializers.StringRelatedField(many=True)
    vertex_2 = serializers.StringRelatedField(many=True)
    #map = serializers.RelatedField(source='map', read_only=True)

    class Meta:
        model = Vertex
        fields = ('id', 'map', 'is_origin_point', 'nfc_code', 'has_nfc',
                  'point_x', 'point_y', 'point_z', 'vertex_1', 'vertex_2')


class SerieSerializerEdge(serializers.ModelSerializer):

    class Meta:
        model = Edge
        fields = ('id', 'name', 'number_floor', 'weight', 'vertex_1', 'vertex_2')
