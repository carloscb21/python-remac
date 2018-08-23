from django.conf.urls import url

from remac_portal.views.apis import map_list, map_detail, vertex_detail, vertex_list, edge_detail, edge_list

urlpatterns = [
    url(r'^maps/$', map_list),
    url(r'^maps/(?P<pk>[0-9]+)/$', map_detail),

    url(r'^maps/(?P<map_id>[0-9]+)/vertexs/$', vertex_list),
    url(r'^maps/(?P<map_id>[0-9]+)/vertexs/(?P<pk>[0-9]+)/$', vertex_detail),

    url(r'^maps/(?P<map_id>[0-9]+)/edges/$', edge_list),
    url(r'^maps/(?P<map_id>[0-9]+)/edges/(?P<pk>[0-9]+)/$', edge_detail),
]

