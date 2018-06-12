#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from remac_portal.core.maps.form.maps import MapForm
from remac_portal.models.maps import Map

"""
FALTA METER UNA FOTOOOOOOOOOOOOOO  AL MAPA
"""


class MapsView(View):

    def get(self, request):

        return render(request, 'maps/map_view.html', context={})


class MapListView(View):

    def get(self, request):
        maps = Map.objects.all()

        return render(request, 'maps/map_list.html', context={
            'maps': maps,
        })


class MapCreateView(View):

    def get(self, request):
        map_form = MapForm()

        return render(request, 'maps/map_create.html', context={
            'map_form': map_form,
            })

    def post(self, request):
        map_form = MapForm(request.POST or None)

        if map_form.is_valid():
            Map.objects.create(
                is_active=map_form.cleaned_data['is_active'],
                name=map_form.cleaned_data['name'],
                numbers_floor=map_form.cleaned_data['numbers_floor'],
                description=map_form.cleaned_data['description'],
            )
            return redirect(reverse('backoffice:list_map'))

        return render(request, 'maps/map_create.html', context={
            'map_form': map_form,
        })


class MapEditView(View):

    def get(self, request, map_id):
        try:
            map = Map.objects.get(id=map_id)

            map_form = MapForm(instance=map)

            return render(request, 'maps/map_create.html', context={
                'map_form': map_form,
                'map': map.id,
            })

        except Map.DoesNotExist:
            raise Http404

    def post(self, request, map_id):
        try:
            map = Map.objects.get(id=map_id)

            map_form = MapForm(request.POST or None, request.FILES or None, instance=map)

            if map_form.is_valid():
                map.is_active = map_form.cleaned_data['is_active']
                map.name = map_form.cleaned_data['name']
                map.numbers_floor = map_form.cleaned_data['numbers_floor']
                map.description = map_form.cleaned_data['description']

                map.save()
                return redirect(reverse('backoffice:list_map'))

            return render(request, 'maps/map_create.html', context={
                'map_form': map_form,
                'map': map.id,
            })

        except Map.DoesNotExist:
            raise Http404


class MapDeleteView(View):

    def get(self, request, map_id):
        try:
            map = Map.objects.get(id=map_id)
            map.delete()

            return redirect(reverse('backoffice:list_map'))

        except Map.DoesNotExist:
            raise Http404

