#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from remac_portal.core.maps.form.vertex import VertexForm
from remac_portal.models.maps import Vertex, Map


class VertexListView(View):

    def get(self, request, map_id):
        try:
            vertexs = Vertex.objects.filter(map_id=map_id)

            return render(request, 'vertex/vertex_list.html', context={
                'vertexs': vertexs,
                'map_id': map_id,
            })
        except Vertex.DoesNotExist:
            raise Http404


class VertexCreateView(View):

    def get(self, request, map_id):
        try:
            map = Map.objects.get(id=map_id)
            vertex_form = VertexForm()

            return render(request, 'vertex/vertex_create.html', context={
                'vertex_form': vertex_form,
                'map_id': map.id,
                })
        except Map.DoesNotExist:
            raise Http404

    def post(self, request, map_id):
        try:
            map = Map.objects.get(id=map_id)
            vertex_form = VertexForm(request.POST or None)

            if vertex_form.is_valid():
                Vertex.objects.create(
                    map=map,
                    is_origin_point=vertex_form.cleaned_data['is_origin_point'],
                    nfc_code=vertex_form.cleaned_data['nfc_code'],
                    name=vertex_form.cleaned_data['name'],
                    has_nfc=vertex_form.cleaned_data['has_nfc'],

                    point_x=vertex_form.cleaned_data['point_x'],
                    point_y=vertex_form.cleaned_data['point_y'],
                    point_z=vertex_form.cleaned_data['point_z'],
                )

                return redirect(reverse('backoffice:list_vertex', args=(map_id)))

            return render(request, 'vertex/vertex_create.html', context={
                'vertex_form': vertex_form,
            })
        except Map.DoesNotExist:
            raise Http404


class VertexEditView(View):

    def get(self, request, map_id, vertex_id):
        try:
            vertex = Vertex.objects.get(id=vertex_id, map_id=map_id)
            vertex_form = VertexForm(instance=vertex)

            return render(request, 'vertex/vertex_create.html', context={
                'vertex_form': vertex_form,
                'vertex': vertex.id,
                'map_id': map_id,
            })

        except Vertex.DoesNotExist:
            raise Http404

    def post(self, request, map_id, vertex_id):
        try:
            vertex = Vertex.objects.get(id=vertex_id, map_id=map_id)

            vertex_form = VertexForm(request.POST or None, request.FILES or None, instance=vertex)

            if vertex_form.is_valid():
                vertex.is_origin_point = vertex_form.cleaned_data['is_origin_point']
                vertex.nfc_code = vertex_form.cleaned_data['nfc_code']
                vertex.name = vertex_form.cleaned_data['name']
                vertex.has_nfc = vertex_form.cleaned_data['has_nfc']
                vertex.has_nfc = vertex_form.cleaned_data['has_nfc']

                vertex.point_x = vertex_form.cleaned_data['point_x']
                vertex.point_y = vertex_form.cleaned_data['point_y']
                vertex.point_z = vertex_form.cleaned_data['point_z']

                vertex.save()
                return redirect(reverse('backoffice:list_vertex', args=(map_id)))

            return render(request, 'vertex/vertex_create.html', context={
                'vertex_form': vertex_form,
                'vertex': vertex.id,
            })

        except Vertex.DoesNotExist:
            raise Http404


class VertexDeleteView(View):

    def get(self, request, map_id, vertex_id):
        try:
            vertex = Vertex.objects.get(id=vertex_id, map_id=map_id)
            vertex.delete()

            return redirect(reverse('backoffice:list_vertex', args=(map_id)))

        except Vertex.DoesNotExist:
            raise Http404

