#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models


BUILDINGCHOICES = (
    ('MARKET', 'Market'),
    ('COMPANY', 'Company'),
    ('HOSPITAL', 'Hospital'),
    ('OTHERS', 'Other'),
)

NFCCHOICES = (
    ('YES', 'Yes'),
    ('No', 'No'),
)

"""
class MapType(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    building = models.CharField(max_length=60, choices=BUILDINGCHOICES, default='OTHERS')

    def __unicode__(self):
        return unicode(self.name)
"""


class Map(models.Model):
    is_active = models.BooleanField(default=False)
    name = models.CharField(max_length=200, unique=True)
    numbers_floor = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    building = models.CharField(max_length=60, choices=BUILDINGCHOICES, default='OTHERS')

    def __unicode__(self):
        return u'%s' % self.name


class Vertex(models.Model):
    map = models.ForeignKey(Map, on_delete=models.CASCADE)
    is_origin_point = models.BooleanField(default=False)
    nfc_code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    has_nfc = models.CharField(max_length=60, choices=NFCCHOICES, default='NO')
    point_x = models.IntegerField(default=0)
    point_y = models.IntegerField(default=0)
    point_z = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%s (%s %s %s)' % (self.name, self.point_x, self.point_y, self.point_z)


class Edge(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    number_floor = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    vertex_1 = models.ForeignKey(Vertex, on_delete=models.CASCADE, related_name='vertex_1')
    vertex_2 = models.ForeignKey(Vertex, on_delete=models.CASCADE, related_name='vertex_2')

    def __unicode__(self):
        return u'%s (%s %s)' % (self.map, self.name, self.weight)