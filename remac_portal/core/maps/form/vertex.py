#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

from remac_portal.models.maps import Vertex


class VertexForm(forms.ModelForm):

    class Meta:
        model = Vertex
        fields = ['is_origin_point', 'nfc_code', 'name', 'has_nfc',
                  'point_x', 'point_y', 'point_z']
