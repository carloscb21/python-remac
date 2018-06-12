#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

from remac_portal.models.maps import MapType


class MapTypeForm(forms.ModelForm):

    class Meta:
        model = MapType
        fields = ['description', 'name', 'building']
