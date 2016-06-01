from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^top_brand_graph$',
            views.top_brand_graph, name='top_brand_graph'),
        url(r'^api/count_items_by_brand$',
            views.count_items_by_brand, name='count_items_by_brand'),
]
