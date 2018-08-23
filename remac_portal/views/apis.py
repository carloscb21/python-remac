from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from remac_portal.models.maps import Vertex, Map, Edge
from remac_portal.core.maps.serializer import SerieSerializerEdge, SerieSerializerMap, SerieSerializerVertex


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def map_list(request):
    """
    List all code serie, or create a new serie.
    """
    if request.method == 'GET':
        maps = Map.objects.all()
        serializer = SerieSerializerMap(maps, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SerieSerializerMap(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def map_detail(request, pk):
    """
    Retrieve, update or delete a serie.
    """
    try:
        map = Map.objects.get(pk=pk)
    except Map.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SerieSerializerMap(map)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SerieSerializerMap(map, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        map.delete()
        return HttpResponse(status=204)


@csrf_exempt
def vertex_list(request, map_id):
    """
    List all code serie, or create a new serie.
    """
    if request.method == 'GET':
        vertexs = Vertex.objects.filter(map_id=map_id)
        serializer = SerieSerializerVertex(vertexs, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SerieSerializerVertex(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def vertex_detail(request, pk, map_id):
    """
    Retrieve, update or delete a serie.
    """
    try:
        vertex = Vertex.objects.get(pk=pk, map_id=map_id)
    except Vertex.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SerieSerializerVertex(vertex)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SerieSerializerVertex(vertex, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        vertex.delete()
        return HttpResponse(status=204)


@csrf_exempt
def edge_list(request, map_id):
    """
    List all code serie, or create a new serie.
    """
    if request.method == 'GET':
        edges = Edge.objects.filter(vertex_1__map_id=map_id)
        serializer = SerieSerializerEdge(edges, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SerieSerializerEdge(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def edge_detail(request, pk, map_id):
    """
    Retrieve, update or delete a serie.
    """
    try:
        edge = Edge.objects.get(pk=pk, vertex_1__map_id=map_id)
    except Edge.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SerieSerializerEdge(edge)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SerieSerializerEdge(edge, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        edge.delete()
        return HttpResponse(status=204)
