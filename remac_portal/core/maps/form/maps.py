#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

from remac_portal.models.maps import Map


class MapForm(forms.ModelForm):

    class Meta:
        model = Map
        fields = ['is_active', 'name', 'numbers_floor', 'description']
