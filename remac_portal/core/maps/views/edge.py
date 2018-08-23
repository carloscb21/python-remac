#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from remac_portal.core.maps.form.edge import EdgeForm
from remac_portal.models.maps import Edge, Map


class EdgeListView(View):

    def get(self, request, map_id):
        try:
            edges = Edge.objects.all()

            return render(request, 'edge/edge_list.html', context={
                'edges': edges,
                'map_id': map_id,
            })
        except Edge.DoesNotExist:
            raise Http404


class EdgeCreateView(View):

    def get(self, request, map_id):
        try:
            map = Map.objects.get(id=map_id)
            edge_form = EdgeForm()

            return render(request, 'edge/edge_create.html', context={
                'edge_form': edge_form,
                'map_id': map.id,
                })
        except Map.DoesNotExist:
            raise Http404

    def post(self, request, map_id):
        try:
            map = Map.objects.get(id=map_id)
            edge_form = EdgeForm(request.POST or None)

            if edge_form.is_valid():
                Edge.objects.create(
                    name=edge_form.cleaned_data['name'],
                    number_floor=edge_form.cleaned_data['number_floor'],
                    weight=edge_form.cleaned_data['weight'],

                    map=map,
                )
                return redirect(reverse('backoffice:list_edge', args=(map.id,)))

            return render(request, 'edge/edge_create.html', context={
                'edge_form': edge_form,
            })
        except Map.DoesNotExist:
            raise Http404


class EdgeEditView(View):

    def get(self, request, map_id, edge_id):
        try:
            edge = Edge.objects.get(id=edge_id)

            edge_form = EdgeForm(instance=edge)

            return render(request, 'edge/edge_create.html', context={
                'edge_form': edge_form,
                'edge': edge.id,
                'map_id': map_id,
            })

        except Edge.DoesNotExist:
            raise Http404

    def post(self, request, edge_id, map_id):
        try:
            edge = Edge.objects.get(id=edge_id)

            edge_form = EdgeForm(request.POST or None, request.FILES or None, instance=edge)

            if edge_form.is_valid():
                edge.name = edge_form.cleaned_data['name']
                edge.number_floor = edge_form.cleaned_data['number_floor']
                edge.weight = edge_form.cleaned_data['weight']

                edge.save()
                return redirect(reverse('backoffice:list_edge', args=(map_id,)))

            return render(request, 'edge/edge_create.html', context={
                'edge_form': edge_form,
                'edge': edge.id,
            })

        except Edge.DoesNotExist:
            raise Http404


class EdgeDeleteView(View):

    def get(self, request, map_id, edge_id):
        try:
            edge = Edge.objects.get(id=edge_id)
            edge.delete()

            return redirect(reverse('backoffice:list_edge', args=(map_id,)))

        except Edge.DoesNotExist:
            raise Http404

