#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

from remac_portal.models.maps import Edge


class EdgeForm(forms.ModelForm):

    class Meta:
        model = Edge
        fields = ['number_floor', 'weight', 'name', 'vertex_1', 'vertex_2']

    def clean_vertex_2(self):
        vertex_1 = self.cleaned_data['vertex_1']
        vertex_2 = self.cleaned_data['vertex_2']
        if vertex_1.id == vertex_2.id:
            raise forms.ValidationError("Edge incorrect: Cant create edge with the same vertex",
                                        code="Edge incorrect")
        else:
            return self.cleaned_data['vertex_2']