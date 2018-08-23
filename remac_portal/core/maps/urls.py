from django.conf.urls import url

from remac_portal.core.maps.views.edge import EdgeListView, EdgeCreateView, EdgeEditView, EdgeDeleteView
from remac_portal.core.maps.views.maps import MapsView, MapListView, MapCreateView, MapEditView, MapDeleteView
#from remac_portal.core.maps.views.type import MapTypeListView, MapTypeDeleteView, MapTypeCreateView, MapTypeEditView
from remac_portal.core.maps.views.vertex import VertexCreateView, VertexListView, VertexEditView, VertexDeleteView

urlpatterns = [
    url(r'^view-maps$', MapsView.as_view(), name='view_maps'),
    
#    url(r'^view-maps/map-type/list', MapTypeListView.as_view(), name='list_map_type'),
#    url(r'^view-maps/map-type/create$', MapTypeCreateView.as_view(), name='create_map_type'),
#    url(r'^view-maps/map-type/(?P<map_type_id>[\w]+)/edit/$', MapTypeEditView.as_view(), name='edit_map_type'),
#    url(r'^view-maps/map-type/(?P<map_type_id>[\w]+)/delete/$', MapTypeDeleteView.as_view(), name='delete_map_type'),

    url(r'^view-maps/map/list', MapListView.as_view(), name='list_map'),
    url(r'^view-maps/map/create$', MapCreateView.as_view(), name='create_map'),
    url(r'^view-maps/map/(?P<map_id>[\w]+)/edit/$', MapEditView.as_view(), name='edit_map'),
    url(r'^view-maps/map/(?P<map_id>[\w]+)/delete/$', MapDeleteView.as_view(), name='delete_map'),

    url(r'^view-maps/map/(?P<map_id>[\w]+)/edge/list', EdgeListView.as_view(), name='list_edge'),
    url(r'^view-maps/map/(?P<map_id>[\w]+)/edge/create$', EdgeCreateView.as_view(), name='create_edge'),
    url(r'^view-maps/map/(?P<map_id>[\w]+)/edge/(?P<edge_id>[\w]+)/edit/$', EdgeEditView.as_view(), name='edit_edge'),
    url(r'^view-maps/map/(?P<map_id>[\w]+)/edge/(?P<edge_id>[\w]+)/delete/$', EdgeDeleteView.as_view(), name='delete_edge'),

    url(r'^view-maps/map/(?P<map_id>[\w]+)/vertex/list', VertexListView.as_view(), name='list_vertex'),
    url(r'^view-maps/map/(?P<map_id>[\w]+)/vertex/create$', VertexCreateView.as_view(), name='create_vertex'),
    url(r'^view-maps/map/(?P<map_id>[\w]+)/vertex/(?P<vertex_id>[\w]+)/edit/$', VertexEditView.as_view(), name='edit_vertex'),
    url(r'^view-maps/map/(?P<map_id>[\w]+)/vertex/(?P<vertex_id>[\w]+)/delete/$',
        VertexDeleteView.as_view(), name='delete_vertex'),

]

