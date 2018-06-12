#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

from remac_portal.models.maps import Edge


class EdgeForm(forms.ModelForm):

    class Meta:
        model = Edge
        fields = ['number_floor', 'weight', 'name']
