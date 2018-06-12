#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from remac_portal.core.maps.form.maps import MapForm
from remac_portal.core.maps.form.type import MapTypeForm
from remac_portal.models.maps import MapType


class MapTypeListView(View):

    def get(self, request):
        map_types = MapType.objects.all()

        return render(request, 'type/map_type_list.html', context={
            'map_types': map_types,
        })


class MapTypeCreateView(View):

    def get(self, request):
        map_type_form = MapTypeForm()

        return render(request, 'type/map_type_create.html', context={
            'map_type_form': map_type_form,
            })

    def post(self, request):
        map_type_form = MapTypeForm(request.POST or None)

        if map_type_form.is_valid():
            MapType.objects.create(
                name=map_type_form.cleaned_data['name'],
                building=map_type_form.cleaned_data['building'],
                description=map_type_form.cleaned_data['description'],
            )
            return redirect(reverse('backoffice:list_map_type'))

        return render(request, 'type/map_type_create.html', context={
            'map_type_form': map_type_form,
        })


class MapTypeEditView(View):

    def get(self, request, map_type_id):
        try:
            map_type = MapType.objects.get(id=map_type_id)

            map_type_form = MapTypeForm(instance=map_type)

            return render(request, 'type/map_type_create.html', context={
                'map_type_form': map_type_form,
                'map_type': map_type.id,
            })

        except MapType.DoesNotExist:
            raise Http404

    def post(self, request, map_type_id):
        try:
            map_type = MapType.objects.get(id=map_type_id)

            map_type_form = MapTypeForm(request.POST or None, request.FILES or None, instance=map_type)

            if map_type_form.is_valid():
                map_type.name = map_type_form.cleaned_data['name']
                map_type.building = map_type_form.cleaned_data['building']
                map_type.description = map_type_form.cleaned_data['description']

                map_type.save()
                return redirect(reverse('backoffice:list_map_type'))

            return render(request, 'type/map_type_create.html', context={
                'map_type_form': map_type_form,
                'map_type': map_type.id,
            })

        except MapType.DoesNotExist:
            raise Http404


class MapTypeDeleteView(View):

    def get(self, request, map_type_id):
        try:
            map_type = MapType.objects.get(id=map_type_id)
            map_type.delete()

            return redirect(reverse('backoffice:list_map_type'))

        except MapType.DoesNotExist:
            raise Http404
